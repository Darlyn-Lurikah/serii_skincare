from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view to show the shopping bag page """

    return render(request, 'bag/bag.html')


# View to add products to bag
def add_to_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    """We get from the POST form data the quantity & 
    redirect (template 'name' attr) """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    """ To keep bag items until browser closed 
    we find var 'bag_session' in session. If its not 
    there, we initialise to empty dict ready for items """
    bag_session = request.session.get('bag_session', {})

    # if item_id matches one in bag_session list
    # ie.in bag already increment quantity
    if item_id in list(bag_session.keys()):
        bag_session[item_id] += quantity
        messages.success(request, f'Updated {product.name} amount to {bag_session[item_id]}in your bag')

    # Else add id to dict ie. add to bag
    else:
        bag_session[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag_session'] = bag_session
    return redirect(redirect_url)


# View to adjust bag quantity within the bag
def adjust_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    """ We get from the POST form data the quantity """
    quantity = int(request.POST.get('quantity'))

    """ To keep bag items until browser closed 
    we find var 'bag_session' in session. If its not 
    there, we initialise to empty dict ready for items """
    bag_session = request.session.get('bag_session', {})
    
    if quantity > 0:
        bag_session[item_id] = quantity
        messages.success(request, f'Updated {product.name} amount to {bag_session[item_id]}in your bag')

    else:
        bag_session.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag_session'] = bag_session
    return redirect(reverse('view_bag'))


# Remove item from the bag
def remove_from_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)

    try:
        bag_session = request.session.get('bag_session', {})

        bag_session.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag_session'] = bag_session
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(staus=500)