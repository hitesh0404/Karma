from django import template
register = template.Library()

@register.filter
def total_price(value):
    result = 0
    for i in value:
        result += (i.product.price_inclusive * i.quantity)
    return result