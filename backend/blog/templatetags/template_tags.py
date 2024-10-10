from django import template

register = template.Library()


@register.filter(name='split')
def split(value, key):
    return value.split(key)

@register.filter(name='get_elem')
def get_elem(value, key):
    return value[int(key)]
