from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

"""Lets queries match product name OR description"""
from django.db.models import Q
from .models import Product, Category

# View for all products page
def all_products(request):
    """ View shows all products, sorting and search queries too"""

    products = Product.objects.all()
    
    """Start with none to avoid errors with empty search bar"""
    query = None
    categories = None

    if request.GET:

        if 'category' in request.GET:

            # Save GET request in var and split by commas
            # to create a list
            categories = request.GET['category'].split(',')

            # Set products var (all products query set)
            # to above list filtered to include
            # category names on said list
            products = products.filter(category__name__in=categories)

            # Converting list of category str. into object list
            # to use in template (show user current category)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter a search!")
                return redirect(reverse('products'))

            """
            Var set to Q obj. where name or description can match query
            i in icontains makes query case insensitive. | = or
            """
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


# View for individual items
def product_detail(request, product_id):
    """ View displays individual products """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
