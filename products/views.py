from django.shortcuts import render, get_object_or_404
from .models import Product

# View for all products page
def all_products(request):
    """ View shows all products, sorting and search queries too"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


# View for individual items
def product_detail(request, product_id):
    """ View displays individual products"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)