from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    # Setting to 0 so theyre always empty to begin
    bag_items = []
    total = 0
    product_count = 0

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
