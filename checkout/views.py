from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Get the bag from the session
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