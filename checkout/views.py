from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from bag.contexts import bag_contents


def checkout(request):
    # Get the bag from the session
    bag_session = request.session.get('bag_session', {})
    if not bag_session:
        # Error message & redirect if nothing in bag 
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    # Save our imported context to a var
    current_bag = bag_contents(request)
    # From context take grand total 
    total = current_bag('grand_total')
    # Round to 0 decimals as Stripe needs integer
    stripe_total = round(total * 100)
    
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