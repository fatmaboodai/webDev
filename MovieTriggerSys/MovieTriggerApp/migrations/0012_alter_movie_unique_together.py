# Generated by Django 4.2 on 2023-05-11 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieTriggerApp', '0011_alter_genre_genre'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together={('genre', 'title')},
        ),
    ]