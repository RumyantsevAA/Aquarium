# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_fish_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='FishTypeID',
            field=models.IntegerField(default=0),
        ),
    ]
