# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import django_markdown.models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, max_length=30, editable=False)),
                ('name', models.CharField(help_text='This name will be used to identify your service.', max_length=100, verbose_name='Service Name')),
                ('additional_info', django_markdown.models.MarkdownField(blank=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(default=b'POINT(0.0 0.0)', help_text='Represented as (longitude, latitude)', srid=4326)),
                ('categories', models.ManyToManyField(to='services.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('order', models.PositiveIntegerField(default=1)),
                ('service', models.ForeignKey(related_name='images', to='services.Service')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
