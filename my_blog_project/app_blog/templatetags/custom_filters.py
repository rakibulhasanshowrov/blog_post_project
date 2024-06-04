from django import template

register = template.Library()

@register.filter(name='range_filter')
def range_filter(value):
    """Returns the first 500 characters followed by '...............'."""
    return value[:500] + '...............'
