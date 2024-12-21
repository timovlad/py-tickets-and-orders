# Generated by Django 4.0.2 on 2024-12-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_user_order_ticket_alter_movie_actors_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='movie',
            name='muvie_title_idx',
        ),
        migrations.AddIndex(
            model_name='movie',
            index=models.Index(fields=['title'], name='movie_title_idx'),
        ),
    ]