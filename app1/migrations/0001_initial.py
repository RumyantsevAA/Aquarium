# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 10:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aquarium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.IntegerField(default=0)),
                ('aquariumVolume', models.IntegerField(default=0)),
                ('totalVolume', models.IntegerField(default=0)),
                ('Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CurrentTime', models.IntegerField(default=0)),
                ('LifeTime', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='FishType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FishName', models.CharField(max_length=30)),
                ('MinLifeTime', models.IntegerField(default=-1)),
                ('MaxLifeTime', models.IntegerField(default=-1)),
                ('LifeVolume', models.IntegerField(default=-1)),
                ('TimeToGoNerest', models.IntegerField(default=-1)),
                ('NerestPeriod', models.IntegerField(default=-1)),
                ('MinFishCountInNerest', models.IntegerField(default=-1)),
                ('MaxNerestCount', models.IntegerField(default=-1)),
                ('DeathRate', models.IntegerField(default=-1)),
                ('DeathRateTime', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('AquariumList', models.ManyToManyField(to='app1.Aquarium')),
                ('SpisokTipovRyb', models.ManyToManyField(to='app1.FishType')),
            ],
        ),
        migrations.AddField(
            model_name='fish',
            name='fishType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.FishType'),
        ),
        migrations.AddField(
            model_name='aquarium',
            name='SpisokRyb',
            field=models.ManyToManyField(to='app1.Fish'),
        ),
        migrations.AddField(
            model_name='aquarium',
            name='Types',
            field=models.ManyToManyField(to='app1.FishType'),
        ),
    ]
