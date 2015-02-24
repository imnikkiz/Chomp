# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0011_recipe_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='response',
            field=jsonfield.fields.JSONField(),
            preserve_default=True,
        ),
    ]
