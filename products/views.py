from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

"""Lets queries match product name OR description"""
from django.db.models import Q
from .models import Product, Category
from django.db.models.functions import Lower
from .forms import ProductForm

# View for all products page
def all_products(request):
    """ View shows all products, sorting and search queries too"""

    products = Product.objects.all()
    
    """Start with none to avoid errors with empty search bar"""
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        # Sorting products by price, rating
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            # To sort products by name instead of id
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)


        # Sorting products by category
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

        # Sorting products by search query
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

    # Var to save in context to send to template
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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


def add_product(request):
    """ To add a product to shop """

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Store the product when save called
            product = form.save()
            # Show added success message
            messages.success(request, f'{product.name} added successfully!')
            # Redirect to product's own page
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        # render instance of product form
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ To edit/update a product in the shop """

    # Get product and product id 
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        # Instantiate form with product (var above)
        form = ProductForm(request.POST, request.FILES, instance=product)
        # Save form if valid
        if form.is_valid():
            form.save()
            # Show success message
            messages.success(request, f'{product.name} updated successfully!')
            # Redirect to updated product's own page
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Product update failed. '
                            'Please ensure the form is correct.'))

    # Create instance of edit form using product
    form = ProductForm(instance=product)
    messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    """ To delete a product from the shop """

    # Get product and product id
    product = get_object_or_404(Product, pk=product_id)
    # Delete product 
    product.delete()
    # Show deleted success message
    messages.success(request, f'{product.name} deleted successfully!')
    # Redirect to all products page
    return redirect(reverse('products'))
