from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    """ Veiw shows all products, sorting and search queries too"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)