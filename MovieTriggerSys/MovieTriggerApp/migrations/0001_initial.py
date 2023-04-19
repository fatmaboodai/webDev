# Generated by Django 4.2 on 2023-04-19 11:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(choices=[('A', 'Action'), ('C', 'Comedy'), ('D', 'Drama'), ('F', 'Fantasy'), ('H', 'Horror'), ('M', 'Mystery'), ('R', 'Romance')], default='D', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('MID', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('age_rating', models.CharField(choices=[('G', 'G'), ('PG', 'PG'), ('PG13', 'PG13'), ('R', 'R')], default='G', max_length=4)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MovieTriggerApp.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Viewer',
            fields=[
                ('VID', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(20)])),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('RID', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Viewer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MovieTriggerApp.viewer')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieTriggerApp.movie')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='trigger',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='MovieTriggerApp.trigger'),
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('LID', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MovieTriggerApp.movie')),
                ('viewer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MovieTriggerApp.viewer')),
            ],
        ),
    ]
