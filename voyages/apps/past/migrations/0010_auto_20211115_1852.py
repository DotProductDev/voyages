# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2021-11-15 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('past', '0009_auto_20211027_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='languagegroup',
            name='modern_country',
        ),
        migrations.AddField(
            model_name='moderncountry',
            name='languages',
            field=models.ManyToManyField(to='past.LanguageGroup'),
        ),
    ]