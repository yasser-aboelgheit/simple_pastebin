# Generated by Django 2.2.2 on 2019-06-27 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paste',
            name='name',
            field=models.CharField(default='Untitled', max_length=200),
        ),
    ]
