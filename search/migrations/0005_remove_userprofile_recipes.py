# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_remove_recipe_time_int'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='recipes',
        ),
    ]
