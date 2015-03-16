# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0020_auto_20150313_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='attribution',
            field=models.CharField(default=b'', max_length=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='display_name',
            field=models.CharField(default=b'', max_length=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_url',
            field=models.CharField(default=b'', max_length=300),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='collection',
            name='day_planned',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
