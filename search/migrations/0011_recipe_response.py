# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0010_auto_20150224_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='response',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
