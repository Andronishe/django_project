from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView,DetailView
from django.shortcuts import render, get_object_or_404
from .models import *


class GamesHome(ListView):
    paginate_by = 5
    model = Games
    template_name = 'store/index.html'
    context_object_name = 'games'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


# def index(request):
#     games = Games.objects.all()
#     context = {
#         'games': games,
#
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#     return render(request, 'store/index.html', context=context)


def about(request):
    return render(request, 'store/about.html', { 'title': 'О сайте'})


# class ShowGame(DetailView):
#     model = Games
#     template_name = 'store/game.html'
#     pk_url_kwarg = 'game_id'
#     context_object_name = 'game'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = context['game']
#         return context



def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def basket(request):
    return HttpResponse("Корзина")


def show_game(request, game_id):
    game = get_object_or_404(Games, pk=game_id)
    store_games = get_object_or_404(Gamestore_games, pk=game_id)
    gamestores = Gamestores.objects.all()
    info = Games.objects.raw(
        'select store_games.id, title,  name, count, price from store_games join store_gamestore_games sgg on store_games.id = sgg.game_id join store_gamestores sg on sg.id = sgg.store_id where store_games.id = "%s" group by title, name, count, price, store_games.id order by title, price',
        [game_id])

    context = {
        'game': game,
        'info': info,
        'title': game.title,
        'cat_selected': game.category_id,
    }

    return render(request, 'store/game.html', context=context)


class GameCategory(ListView):
    paginate_by = 5
    model = Games
    template_name = 'store/index.html'
    context_object_name = 'games'
    allow_empty = False

    def get_queryset(self):
        return Games.objects.filter(category__id=self.kwargs['cat_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['games'][0].category)
        return context


# def show_category(request, cat_id):
#     games = Games.objects.filter(category=cat_id)
#     if len(games) == 0:
#         raise Http404()
#
#     context = {
#         'games': games,
#         'title': 'Отоброжение по рубрикам',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'store/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
