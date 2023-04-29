from django import template

register = template.Library()


@register.filter(name='year')
def year(value):
    """
    фильтр добавляет 'г.'
    """
    return f'{value} г.'
