# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0012_auto_20150310_0223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planner',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='planner',
            field=models.OneToOneField(related_name='planner', null=True, default=None, to='search.Planner'),
            preserve_default=True,
        ),
    ]
