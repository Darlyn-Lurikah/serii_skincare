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
    }

    return render(request, template, context)