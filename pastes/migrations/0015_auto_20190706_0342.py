# Generated by Django 2.2.3 on 2019-07-06 01:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pastes', '0014_auto_20190705_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='paste',
            name='author',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='paste',
            name='allow',
            field=models.ManyToManyField(to='pastes.Test'),
        ),
        migrations.AlterField(
            model_name='test',
            name='allowed',
            field=models.CharField(blank=True, choices=[('yasser', 'yasser'), ('yasser2', 'yasser2'), ('yasser3', 'yasser3'), ('yasser4', 'yasser4'), ('yasser5', 'yasser5')], max_length=200, null=True),
        ),
    ]
