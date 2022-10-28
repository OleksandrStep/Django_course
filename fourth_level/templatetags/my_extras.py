from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out add values of arg from the string!
    :param value:
    :param arg:
    :return:
    """
    return value.repalace(arg, '')


# register.filter('cut', cut)
