from django import template
import re

register = template.Library()

@register.filter(name='split')
def split(value, key):
    return value.split(key)

@register.filter(name='get_elem')
def get_elem(value, key):
    return value[int(key)]

@register.filter(name='delete_gap')
def delete_gap(value):
    return re.sub("^\s+|\n|\r|\s+$", '', value)