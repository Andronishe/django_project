# Generated by Django 4.0.3 on 2022-04-30 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0004_alter_games_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game_category',
            old_name='category',
            new_name='name',
        ),
        migrations.AddField(
            model_name='games',
            name='favourites',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gamestore_games',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gsg2game', to='store.games'),
        ),
    ]
