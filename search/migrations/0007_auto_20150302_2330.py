# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20150302_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='date_planned',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
