# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-30 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20180310_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False, verbose_name='Order'),
        ),
    ]
