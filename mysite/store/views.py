import datetime
import io

import xlwt
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse, FileResponse
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from reportlab.lib.units import inch
from django.core import serializers

from .models import *
from .forms import *
import json
from reportlab.pdfgen import canvas



# class GamesHome(ListView):
#     paginate_by = 5
#     model = Games
#     form_class = GamesFilter
#     template_name = 'store/index.html'
#     context_object_name = 'games'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Главная страница'
#         # context['form'] = GamesFilter
#         return context


def index(request):
    # gs_games = Gamestore_games.objects.values_list().select_related('game')
    games = Games.objects.all()
    form = GamesFilter(request.GET)
    if form.is_valid():
        if form.cleaned_data['min_price']:
            games = games.filter(gsg2game__price__gte=form.cleaned_data["min_price"]).distinct()
            print(games)

        if form.cleaned_data['max_price']:
            games = games.filter(gsg2game__price__lte=form.cleaned_data["max_price"]).distinct()

        if form.cleaned_data['ordering']:
            games = games.order_by(form.cleaned_data['ordering'])
    context = {
        'games': games,
        # 'gs_games': gs_games,
        'form': form,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'store/index.html', context=context)


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


def addgame(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'store/addgame.html', {'form': form, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse("Обратная связь")


# def login(request):
#     return HttpResponse("Авторизация")


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
        return Games.objects.filter(category__id=self.kwargs['cat_id']).select_related('category')

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


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'store/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'store/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class Search(ListView):
    model = Games
    template_name = "store/index.html"
    context_object_name = 'games'

    def get_queryset(self):
        games = Games.objects.filter(title__icontains=self.request.GET.get('search'))
        return games

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Поиск'
        return context


# def jsn(request):
#     data = list(Games.objects.values())
#     return JsonResponse(data, safe=False)
#     model = serializers.serialize('json', Games.objects.all())
#     data = {'model': model}
#     return JsonResponse(data)


def game_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)

    lines = []
    games = Games.objects.all()
    for game in games:
        lines.append(game.title)
        lines.append(game.author.company)
        lines.append(str(game.publish_date))
        lines.append(game.category.name)
        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='games.pdf')


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=game_excel' + str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('game_excel')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Title', 'Author', 'Category', 'Publish_date']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Games.objects.values_list('title', 'author', 'category', 'publish_date')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response