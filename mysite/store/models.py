from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Gamestores(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name='навзвание')
    web_site = models.CharField(max_length=100,  verbose_name='веб-сайт')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Магазин видеоигр"
        verbose_name_plural = "Магазины Видеоигр"
        ordering = ["id", "name"]


class Game_category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["id"]

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class Games_authors(models.Model):
    company = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ["id", "company"]


# class Users(models.Model):
#     login = models.CharField(max_length=40, verbose_name='имя пользователя')
#     password = models.CharField(max_length=40, verbose_name='пароль')
#
#     class Meta:
#         verbose_name = "Пользователь"
#         verbose_name_plural = "Пользователи"
#         ordering = ["login"]


class Games(models.Model):
    author = models.ForeignKey(Games_authors, on_delete=models.PROTECT, verbose_name='автор')
    title = models.CharField(max_length=100, verbose_name='название')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, verbose_name='фото')
    publish_date = models.DateField(auto_now_add=True, verbose_name='публикация')
    category = models.ForeignKey(Game_category, on_delete=models.DO_NOTHING, verbose_name='категория')
    favourites = models.ManyToManyField(User, related_name='favourites', default=None, blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('game', kwargs={'game_id': self.pk})

    class Meta:
        verbose_name = "Видеоигры"
        verbose_name_plural = "Видеоигры"
        ordering = ["publish_date", "title"]


class Gamestore_games(models.Model):
    store = models.ForeignKey(Gamestores, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE, related_name='gsg2game')
    count = models.IntegerField(verbose_name='количество')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="цена")

    def __str__(self):
        return str(self.price)

    class Meta:
        verbose_name = "Игры в магазинах"
        verbose_name_plural = "Игры в магазинах"
        ordering = ["price", "count"]


# class Gamestore_sold_games(models.Model):
#     store = models.ForeignKey(Gamestores, on_delete=models.CASCADE)
#     game = models.ForeignKey(Games, on_delete=models.DO_NOTHING)
#     user = models.ForeignKey(Users, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='цена')
#     insert_date = models.DateField(auto_now_add=True, verbose_name='дата добавления')
#     update_date = models.DateField(auto_now=True, verbose_name='дата обновления')
#
#     class Meta:
#         verbose_name = "Проданные игры"
#         verbose_name_plural = "Проданные игры"
#         ordering = ["price", "insert_date"]