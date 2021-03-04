# Generated by Django 3.1.3 on 2021-02-21 19:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogApp', '0007_auto_20210217_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, default='', to=settings.AUTH_USER_MODEL),
        ),
    ]
