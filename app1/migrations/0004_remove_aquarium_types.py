# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 11:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_aquarium_spisokryb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aquarium',
            name='Types',
        ),
    ]
