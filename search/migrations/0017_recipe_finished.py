# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0016_auto_20150313_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='finished',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
