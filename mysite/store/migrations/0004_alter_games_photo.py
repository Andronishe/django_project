# Generated by Django 4.0.3 on 2022-04-18 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_game_category_options_alter_games_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', verbose_name='фото'),
        ),
    ]
