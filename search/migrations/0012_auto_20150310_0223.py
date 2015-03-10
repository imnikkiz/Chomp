# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0011_food_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_profile', models.OneToOneField(related_name='planner', to='search.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='collection',
            name='planner',
            field=models.ForeignKey(related_name='recipes', blank=True, to='search.Planner', null=True),
            preserve_default=True,
        ),
    ]
