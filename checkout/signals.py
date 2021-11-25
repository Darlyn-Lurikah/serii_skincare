from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


# Decorator to say 
# (signal_being_recieved, sender=FromWhichModel)
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    To update our order total on a lineitem update/create
    """
    # Call update_total on the order this
    # specific line item (instance) is related to
    instance.order.update_total()


# Decorator to say 
# (signal_being_recieved, sender=FromWhichModel)
@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    """
    To update our order total on a lineitem delete
    """
    instance.order.update_total()
