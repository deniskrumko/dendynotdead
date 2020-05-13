# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-26 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audiofiles', '0002_auto_20170101_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiotrack',
            name='description',
        ),
        migrations.AddField(
            model_name='audiotrack',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='English description'),
        ),
        migrations.AddField(
            model_name='audiotrack',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Russian description'),
        ),
    ]
