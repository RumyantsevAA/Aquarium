# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20160424_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='Name',
            field=models.CharField(default='fish', max_length=30),
            preserve_default=False,
        ),
    ]