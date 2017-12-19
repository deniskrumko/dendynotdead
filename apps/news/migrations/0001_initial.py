# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 14:20
from __future__ import unicode_literals

import apps.core.models
import autoslug.fields
from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=('title',), verbose_name='Slug')),
                ('preview', models.TextField(blank=True, null=True, verbose_name='Preview')),
                ('full_text', models.TextField(blank=True, null=True, verbose_name='Full text')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.core.models.BaseModel.file_upload_path, verbose_name='Image')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Views')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
    ]
