from django import template


# We have to register this template 
register = template.Library()

# To calculate the subtotal of each item in bag
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
