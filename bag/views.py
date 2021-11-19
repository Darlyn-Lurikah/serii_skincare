from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view to show the shopping bag page """

    return render(request, 'bag/bag.html')


# View to add products to bag
def add_to_bag(request, item_id):

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

    # Else add id to dict ie. add to bag
    else:
        bag_session[item_id] = quantity

    request.session['bag_session'] = bag_session
    return redirect(redirect_url)