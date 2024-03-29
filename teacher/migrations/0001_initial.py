# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(default='1', max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('avatar', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TrainedTopics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainedTopics', models.CharField(max_length=30)),
            ],
        ),
    ]
