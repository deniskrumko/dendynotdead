# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-16 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20180310_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='obfuscate_filename',
            field=models.BooleanField(default=True, verbose_name='Obfuscate filename'),
        ),
    ]