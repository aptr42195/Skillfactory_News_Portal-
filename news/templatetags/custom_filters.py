from django import template

register = template.Library()


@register.filter(name='year')
def year(value):
    """
    Фильтр добавляет 'г.'
    """
    return f'{value} г.'