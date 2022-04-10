from django.http import HttpResponse, HttpResponseNotFound, Http404

from django.shortcuts import render

from .models import *

menu = [{'title': "Главная страница", 'url_name': 'home'},
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    games = Games.objects.all()
    cats = Game_category.objects.all()
    context = {
        'posts': games,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'store/index.html',
                  {'games': games, 'cats': cats, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'store/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_game(request, game_id):
    return HttpResponse(f"Отображение игры с id = {game_id}")


def show_category(request, cat_id):
    games = Games.objects.filter(category=cat_id)
    cats = Game_category.objects.all()
    if len(games) == 0:
        raise Http404()

    context = {
        'games': games,
        'cats': cats,
        'menu': menu,
        'title': 'Отоброжение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'store/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
