# Generated by Django 2.2.3 on 2019-07-06 06:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastes', '0018_paste_privacy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='allow',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
