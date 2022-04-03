from django.db import models


class Gamestores(models.Model):
    name = models.CharField(max_length=100, null=False)
    web_site = models.CharField(max_length=100)



class Game_category(models.Model):
    category = models.CharField(max_length=100)



class Games_authors(models.Model):
    company = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


class Users(models.Model):
    login = models.CharField(max_length=40)
    password = models.CharField(max_length=40)


class Games(models.Model):
    author = models.ForeignKey(Games_authors, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    publish_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Game_category, on_delete=models.DO_NOTHING)


class Gamestore_games(models.Model):
    store = models.ForeignKey(Gamestores, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Gamestore_sold_games(models.Model):
    store = models.ForeignKey(Gamestores, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    insert_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)