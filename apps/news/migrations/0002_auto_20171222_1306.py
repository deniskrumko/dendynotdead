# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-22 13:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news_author', to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='news',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='news_likes', to=settings.AUTH_USER_MODEL, verbose_name='Likes'),
        ),
        migrations.AddField(
            model_name='news',
            name='show_image_on_preview',
            field=models.BooleanField(default=True, verbose_name='Show image on preview'),
        ),
    ]