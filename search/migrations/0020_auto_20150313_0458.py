# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0019_recipe_attributes_dict'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='attributes_dict',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='finished',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient_lines',
        ),
    ]
