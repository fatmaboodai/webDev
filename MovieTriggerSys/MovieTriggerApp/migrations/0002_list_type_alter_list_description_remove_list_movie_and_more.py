# Generated by Django 4.2 on 2023-05-10 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MovieTriggerApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='type',
            field=models.CharField(choices=[('WL', 'Watch List'), ('W', 'Watched'), ('F', 'Favorites'), ('B', 'Blocked')], default='WL', max_length=255),
        ),
        migrations.AlterField(
            model_name='list',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='list',
            name='movie',
        ),
        migrations.AlterField(
            model_name='list',
            name='viewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieTriggerApp.viewer'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='trigger',
        ),
        migrations.AlterField(
            model_name='review',
            name='Viewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieTriggerApp.viewer'),
        ),
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trigger',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('Viewer', 'movie')},
        ),
        migrations.AddField(
            model_name='list',
            name='movie',
            field=models.ManyToManyField(to='MovieTriggerApp.movie'),
        ),
        migrations.AddField(
            model_name='movie',
            name='trigger',
            field=models.ManyToManyField(blank=True, null=True, to='MovieTriggerApp.trigger'),
        ),
    ]