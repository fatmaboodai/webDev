# Generated by Django 4.2 on 2023-04-23 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieTriggerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='LID',
            field=models.CharField(auto_created=True, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='MID',
            field=models.CharField(auto_created=True, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='RID',
            field=models.CharField(auto_created=True, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='viewer',
            name='VID',
            field=models.CharField(auto_created=True, max_length=255, primary_key=True, serialize=False),
        ),
    ]
