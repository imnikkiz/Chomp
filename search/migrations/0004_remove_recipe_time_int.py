# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_course_cuisine_holiday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='time_int',
        ),
    ]
