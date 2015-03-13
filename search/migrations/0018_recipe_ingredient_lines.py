# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0017_recipe_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredient_lines',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
