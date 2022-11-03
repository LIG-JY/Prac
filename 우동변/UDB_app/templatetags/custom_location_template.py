from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)  #  key에 해당하는 value를 return