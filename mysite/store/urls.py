from django.urls import path

from .views import *

urlpatterns = [
    path('', GamesHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('basket/', basket, name='basket'),
    path('game/<int:game_id>/', show_game, name='game'),
    path('category/<int:cat_id>/', GameCategory.as_view(), name='category'),
]
