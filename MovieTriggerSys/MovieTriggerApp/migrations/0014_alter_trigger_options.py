# Generated by Django 4.2.1 on 2023-05-12 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieTriggerApp', '0013_viewer_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trigger',
            options={'permissions': [('edit_trigger', 'Can edit trigger')]},
        ),
    ]