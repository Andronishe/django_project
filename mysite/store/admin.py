from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *


@admin.register(Games)
class GamesAdmin(ImportExportModelAdmin):
    list_display=('id', 'title', 'author', 'photo', 'publish_date')
    list_display_links=('id', 'title')
    search_fields = ('title', 'author')


@admin.register(Game_category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Gamestores)
class GamestoresAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'web_site')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Games_authors)
class AuthorsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'company', 'email')
    list_display_links = ('id', 'company')
    search_fields = ('company', 'email')


@admin.register(Gamestore_games)
class GamestoreGamesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'store', 'game', 'count', 'price')
    list_display_links = ('count', 'price')
    search_fields = ('price',)


# @admin.register(Gamestore_sold_games)
# class GamestoreSoldGamesAdmin(ImportExportModelAdmin):
#     list_display = ('id', 'store', 'game', 'price', 'insert_date', 'insert_date')
#     search_fields = ('price',)


class UserAdmin(ImportExportModelAdmin):
    list_display = ('id', 'login', 'password')
    list_display_links = ('login',)
    search_fields = ('login',)


# admin.site.register(Games, GamesAdmin)
# admin.site.register(Game_category, CategoryAdmin)
# admin.site.register(Gamestores, GamestoresAdmin)
# admin.site.register(Games_authors, AuthorsAdmin)
# admin.site.register(Gamestore_games, GamestoreGamesAdmin)
# admin.site.register(Gamestore_sold_games, GamestoreSoldGamesAdmin)
# admin.site.register(Users, UserAdmin)
