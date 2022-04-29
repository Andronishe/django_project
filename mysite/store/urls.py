from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('addgame/', addgame, name='add_game'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('search/', Search.as_view(), name='search'),
    path('basket/', basket, name='basket'),
    #path('jsn/', jsn, name='jsn'),
    path('game_pdf/', game_pdf, name='game_pdf'),
    path('export_excel/', export_excel, name='export_excel'),
    path('game/<int:game_id>/', show_game, name='game'),
    path('category/<int:cat_id>/', GameCategory.as_view(), name='category'),
]
