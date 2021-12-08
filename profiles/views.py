from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order

@login_required
def profile(request):
     
    profile = get_object_or_404(UserProfile, user=request.user)

    """To post user profile form and update it"""
    if request.method == 'POST':
        # Create new instance of profile form w/ post data
        form = UserProfileForm(request.POST, instance=profile)
        # If valid, save and show success message
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

   

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    # Get the order from order no. in Order model
    order = get_object_or_404(Order, order_number=order_number)

    # Message to inform its a past order
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        f'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
