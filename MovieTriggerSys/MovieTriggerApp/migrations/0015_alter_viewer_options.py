# Generated by Django 4.2.1 on 2023-05-15 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieTriggerApp', '0014_alter_trigger_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='viewer',
            options={'permissions': [('view_users', 'Can view users')]},
        ),
    ]
