from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

import stripe
import json

from products.models import Product
from bag.contexts import bag_contents
from .forms import OrderForm
from .models import Order, OrderLineItem


def cache_checkout_data(request):
    try:
        # Take payment intent id from splitting
        # client secret from payment intent
        pid = request.POST.get('client_secret').split('_secret')[0]
        # Set up stripe key to modify pay intent 
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Modify pay intent to add this info
        stripe.PaymentIntent.modify(pid, metadata={
            'bag_session': json.dumps(request.session.get('bag_session', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    # If there an error, show message
    except Exception as e:
        messages.error(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=e, status=400)



def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # Get the bag from the session
        bag_session = request.session.get('bag_session', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        # Create form instance w/ checkout form data
        order_form = OrderForm(form_data)

        # If form valid, save order
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag_session)
            order.save()
            # Iterate through bag items to create
            # each line item
            for item_id, item_data in bag_session.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                # If order doesnt exist, show message     
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't "
                        "found in our database. "
                        "Please call us for assistance!")
                    )
                    # Delete nonexistent order & redirect
                    order.delete()
                    return redirect(reverse('view_bag'))
         
            # Option to save info to user profile
            request.session['save_info'] = 'save-info' in request.POST
            # Redirect to order success page
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            # If order form not valid, show message
            messages.error(request, ('There was an error with your form. '
                                     'Please double check your information.'))


    else:
        bag_session = request.session.get('bag_session', {})
        if not bag_session:
            # Error message & redirect if nothing in bag
            messages.error(request, "Your bag is empty")
            return redirect(reverse('products'))

        # Save our imported context to a var
        current_bag = bag_contents(request)
        # From context take grand total key
        total = current_bag['grand_total']
        # Round to 0 decimals as Stripe needs integer
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        # Create and give payintent our total and currency 
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )


    # Create instance of OrderForm
    order_form = OrderForm()

    #  Alert if public key forgotten
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    # Save instance var in context
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    # Check if user saved info to profile
    save_info = request.session.get('save_info')
    # Get order no.
    order = get_object_or_404(Order, order_number=order_number)

    # Success message
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag_session' in request.session:
        del request.session['bag_session']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
