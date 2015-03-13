# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0018_recipe_ingredient_lines'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='attributes_dict',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
