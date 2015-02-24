# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_auto_20150223_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingredient_string', models.CharField(default=b'', max_length=300)),
                ('recipe', models.ForeignKey(to='search.Recipe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
