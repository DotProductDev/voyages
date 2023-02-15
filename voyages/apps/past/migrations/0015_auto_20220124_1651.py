# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2022-01-24 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('past', '0014_auto_20220114_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enslavervoyageconnectionsource',
            name='enlaver_voyage_connection',
        ),
        migrations.RemoveField(
            model_name='enslavervoyageconnectionsource',
            name='source',
        ),
        migrations.AlterField(
            model_name='enslaved',
            name='post_disembark_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='voyage.Place'),
        ),
        migrations.AlterField(
            model_name='enslavementrelation',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='voyage.Place'),
        ),
        migrations.AlterField(
            model_name='enslaveralias',
            name='identity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aliases', to='past.EnslaverIdentity'),
        ),
        migrations.AlterField(
            model_name='enslaveridentity',
            name='birth_place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='voyage.Place'),
        ),
        migrations.AlterField(
            model_name='enslaveridentity',
            name='death_place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='voyage.Place'),
        ),
        migrations.AlterField(
            model_name='enslavermerger',
            name='birth_place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='voyage.Place'),
        ),
        migrations.AlterField(
            model_name='enslavermerger',
            name='death_place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='voyage.Place'),
        ),
        migrations.DeleteModel(
            name='EnslaverVoyageConnectionSource',
        ),
    ]