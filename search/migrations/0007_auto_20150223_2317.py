# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20150223_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='big_img',
            field=models.CharField(default=b'', max_length=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='lil_img',
            field=models.CharField(default=b'', max_length=300),
            preserve_default=True,
        ),
    ]
