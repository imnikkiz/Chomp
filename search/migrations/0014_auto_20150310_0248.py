# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0013_auto_20150310_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='planner',
            field=models.OneToOneField(related_name='user_profile', null=True, default=None, to='search.Planner'),
            preserve_default=True,
        ),
    ]
