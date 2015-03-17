# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'search', '0001_initial'), (b'search', '0002_keyword_text'), (b'search', '0003_recipe'), (b'search', '0004_auto_20150220_2156'), (b'search', '0005_auto_20150221_0022'), (b'search', '0006_auto_20150223_2313'), (b'search', '0007_auto_20150223_2317'), (b'search', '0008_auto_20150223_2324'), (b'search', '0009_ingredient'), (b'search', '0010_auto_20150224_0056'), (b'search', '0011_recipe_response'), (b'search', '0012_auto_20150224_0119'), (b'search', '0013_auto_20150224_2358'), (b'search', '0014_remove_search_response'), (b'search', '0015_auto_20150225_0148')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200)),
                ('yummly_id', models.CharField(default=b'', max_length=300)),
                ('number_of_servings', models.IntegerField(null=True, blank=True)),
                ('servings_as_string', models.CharField(default=b'', max_length=100, null=True, blank=True)),
                ('time_int', models.IntegerField(null=True, blank=True)),
                ('time_string', models.CharField(default=b'', max_length=100, null=True, blank=True)),
                ('big_img', models.CharField(default=b'', max_length=300, null=True, blank=True)),
                ('lil_img', models.CharField(default=b'', max_length=300, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyword', models.CharField(default=b'', max_length=200)),
                ('recipes', models.ManyToManyField(related_name='searches', to=b'search.Recipe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingredient_string', models.CharField(default=b'', max_length=300, null=True, blank=True)),
                ('recipe', models.ForeignKey(related_name='ingredients', to='search.Recipe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recipes', models.ManyToManyField(related_name='profiles', to=b'search.Recipe')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        # migrations.RemoveField(
        #     model_name='recipe',
        #     # name='response',
        # ),
    ]
