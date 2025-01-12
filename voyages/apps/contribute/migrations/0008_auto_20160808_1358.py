# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contribute', '0007_auto_20160805_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditorVoyageContribution',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('notes',
                 models.TextField(help_text='Editor notes',
                                  max_length=10000,
                                  null=True,
                                  verbose_name='Notes')),
                ('final_decision', models.IntegerField(default=0)),
                ('published',
                 models.BooleanField(
                     default=False,
                     help_text='The contribution has been published to the '
                     'database')),
                ('interim_voyage',
                 models.ForeignKey(related_name='+',
                                   to='contribute.InterimVoyage',
                                   null=True,
                                   on_delete=models.CASCADE)),
                ('request',
                 models.ForeignKey(related_name='editor_contribution',
                                   to='contribute.ReviewRequest',
                                   on_delete=models.CASCADE)),
            ],
        ),
        migrations.AlterField(
            model_name='reviewvoyagecontribution',
            name='notes',
            field=models.TextField(help_text='Reviewer notes',
                                   max_length=10000,
                                   null=True,
                                   verbose_name='Notes'),
        ),
    ]
