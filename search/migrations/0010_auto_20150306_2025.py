# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0009_auto_20150306_2022'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FoodCategory',
            new_name='Category',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='food',
            field=models.ForeignKey(related_name='ingredients', to='search.Food', null=True),
            preserve_default=True,
        ),
    ]
