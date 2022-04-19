from django.contrib import admin

from .models import *


class GamesAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'author', 'photo', 'publish_date')
    list_display_links=('id', 'title')
    search_fields = ('title', 'author')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class GamestoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'web_site')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'email')
    list_display_links = ('id', 'company')
    search_fields = ('company', 'email')


class GamestoreGamesAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'game', 'count', 'price')
    list_display_links = ('count', 'price')
    search_fields = ('price',)


class GamestoreSoldGamesAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'game', 'price', 'insert_date', 'insert_date')
    search_fields = ('price',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'password')
    list_display_links = ('login',)
    search_fields = ('login',)


admin.site.register(Games, GamesAdmin)
admin.site.register(Game_category, CategoryAdmin)
admin.site.register(Gamestores, GamestoresAdmin)
admin.site.register(Games_authors, AuthorsAdmin)
admin.site.register(Gamestore_games, GamestoreGamesAdmin)
admin.site.register(Gamestore_sold_games, GamestoreSoldGamesAdmin)
admin.site.register(Users, UserAdmin)
