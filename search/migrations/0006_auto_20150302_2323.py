# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_remove_userprofile_recipes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_planned', models.DateField(blank=True)),
                ('recipe', models.ForeignKey(to='search.Recipe')),
                ('user_profile', models.ForeignKey(to='search.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='recipes',
            field=models.ManyToManyField(related_name='profiles', through='search.Collection', to='search.Recipe'),
            preserve_default=True,
        ),
    ]
