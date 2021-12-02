from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    # Get the bag from the session
    bag_session = request.session.get('bag_session', {})
    if not bag_session:
        # Error message & redirect if nothing in bag 
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    # Create instance of OrderForm
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    # Save instance var in context
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K0c31Aq3O84xn4PwlatDYNoxJHeaIn5ToIfE22gGEFLOJQfSGDbBVS6Y3Z2azCgflWikSZyhflBR7C9bCid8AR100IEjjCneL',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)