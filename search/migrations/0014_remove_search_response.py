# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0013_auto_20150224_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='response',
        ),
    ]
