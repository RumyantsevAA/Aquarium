# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-15 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20160424_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='Name',
            field=models.CharField(default=id, max_length=30),
        ),
    ]
