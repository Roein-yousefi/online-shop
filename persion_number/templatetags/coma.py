from django import template

register = template.Library()

@register.filter
def intcomma_custom(value):
    value = int(value)
    return '{:,.0f}'.format(value)
