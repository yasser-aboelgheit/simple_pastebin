# Generated by Django 2.2.3 on 2019-07-04 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastes', '0008_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
