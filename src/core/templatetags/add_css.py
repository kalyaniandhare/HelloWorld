"""
Add CSS
"""
from django import template

register = template.Library()  # pylint: disable=invalid-name


@register.filter(name='add_css')
def add_css(value, arg):
    """
    Add CSS
    """
    return value.as_widget(attrs={'class': arg})
