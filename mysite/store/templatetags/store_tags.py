from django import template
from store.models import *
register = template.Library()


@register.simple_tag()
def get_categories():
    return Game_category.objects.all()


@register.inclusion_tag('store/list_categories.html')
def show_categories():
    cats = Game_category.objects.all()
    return {"cats": cats}


@register.simple_tag()
def get_menu():
    menu = [{'title': "Главная страница", 'url_name': 'home'},
            {'title': "О сайте", 'url_name': 'about'},
            {'title': "Обратная связь", 'url_name': 'contact'},
            {'title': "Корзина", 'url_name': 'basket'},
            {'title': "Войти", 'url_name': 'login'}
            ]
    return menu
