from django import template

register = template.Library()

@register.filter
def comments_only_tags(comments):
    return comments.filter(active=True)