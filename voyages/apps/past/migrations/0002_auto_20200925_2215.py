# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-09-25 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('past', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enslaved',
            name='modern_name_first',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='enslaved',
            name='modern_name_second',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='enslaved',
            name='modern_name_third',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
