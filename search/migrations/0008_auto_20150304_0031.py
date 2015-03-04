# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_auto_20150302_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='amount',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='food',
            field=models.CharField(default=b'', max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='food_category',
            field=models.ForeignKey(related_name='foods', to='search.FoodCategory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='measurement',
            field=models.CharField(default=b'', max_length=100, null=True),
            preserve_default=True,
        ),
    ]
