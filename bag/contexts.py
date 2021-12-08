from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    # Setting to 0 so theyre always empty to begin
    bag_items = []
    total = 0
    product_count = 0

    # Take bag session to access bag data
    # anywhere & display in cart anywhere
    bag_session = request.session.get('bag_session', {})

    for item_id, quantity in bag_session.items():
        # Get product obj (all product data)
        product = get_object_or_404(Product, pk=item_id)
        # total incremented by quantity x price
        total += quantity * product.price
        # product count incremented by quantity
        product_count += quantity
        # Add dict to bag items
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # Checking if user gets free delivery
    if total < settings.FREE_DELIVERY_THRESHOLD:
        # Delivery is total x 0.1 (10/100) if under free
        # delivery threshold
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

        # Show user how much to free delivery
        # but subtracting threshold from total
        amount_to_free_delivery = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        # if threshold met
        delivery = 0
        amount_to_free_delivery = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'amount_to_free_delivery': amount_to_free_delivery,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
