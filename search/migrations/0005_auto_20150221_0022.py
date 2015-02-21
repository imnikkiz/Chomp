# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20150220_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='recipes',
            field=models.ManyToManyField(related_name='searches', to='search.Recipe'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='search',
            name='response',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
