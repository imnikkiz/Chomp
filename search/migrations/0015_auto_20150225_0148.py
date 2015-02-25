# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0014_remove_search_response'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='response',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='recipes',
            field=models.ManyToManyField(related_name='profiles', to='search.Recipe'),
            preserve_default=True,
        ),
    ]
