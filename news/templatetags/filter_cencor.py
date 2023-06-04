from django import template

register = template.Library()

stop_words = [
    'плохоеслово1',
    'плохоеслово2',
    'плохоеслово3',
    'плохоеслово4',
    'плохоеслово5',
]


@register.filter(name='cencor')
def cencor(value):
    """
    Функция принимает текст, заменяет 'плохие слова'
    на символ '*'
    """
    for i in stop_words:
        value = value.replace(i.lower(), '*')
    return value