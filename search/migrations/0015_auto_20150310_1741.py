# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0014_auto_20150310_0248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='date_planned',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='planner',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='planner',
        ),
        migrations.DeleteModel(
            name='Planner',
        ),
        migrations.AddField(
            model_name='collection',
            name='day_planned',
            field=models.CharField(default=b'', max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='collection',
            name='meal_planned',
            field=models.CharField(default=b'', max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
