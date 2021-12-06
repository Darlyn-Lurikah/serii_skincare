from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm

def profile(request):
     
    profile = get_object_or_404(UserProfile, user=request.user)

    """To post user profile form"""
    if request.method == 'POST':
        # Create new instance of profile form w/ post data
        form = UserProfileForm(request.POST, instance=profile)
        # If valid, save and show success message
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(request.POST, instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }
    
    return render(request, template, context)
