from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

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
        order_form = OrderForm(form_data),

        # If form valid, save order
        if order_form.is_valid():
            order.save()
            # Iterate through bag items to create
            # each line item
            for item_id, item_data in bag.items():
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