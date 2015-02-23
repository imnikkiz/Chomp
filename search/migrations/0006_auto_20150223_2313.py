# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20150221_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='number_of_servings',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='servings_as_string',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='time_int',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='time_string',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
