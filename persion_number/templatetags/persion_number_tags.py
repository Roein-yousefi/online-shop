from django import template

register = template.Library()

@register.filter
def persion_number_tag(number):
    number = str(number)
    number_trans = number.maketrans('0123456789' , '۰۱۲۳۴۵۶۷۸۹')
    return number.translate(number_trans)