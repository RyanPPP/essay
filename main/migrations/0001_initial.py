# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 11:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Essay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='no title', max_length=100)),
                ('due_time', models.DateField(default='2017-01-01')),
                ('description', models.CharField(default='no description', max_length=200)),
                ('type', models.CharField(choices=[('AT', 'Autonomous'), ('PL', 'Plan')], default='AT', max_length=2)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isOffTopic', models.BooleanField()),
                ('score', models.CharField(max_length=5)),
                ('error', jsonfield.fields.JSONField()),
                ('chart1', jsonfield.fields.JSONField()),
                ('chart2', jsonfield.fields.JSONField()),
                ('detail', jsonfield.fields.JSONField()),
                ('feedback', models.CharField(default='\u65e0', max_length=50)),
                ('essay_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Essay')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('actual_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('avatar', models.CharField(max_length=30)),
                ('exp', models.IntegerField()),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='User_Essay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(default=django.utils.timezone.now, verbose_name='\u4fdd\u5b58\u65e5\u671f')),
                ('update_date', models.DateField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65e5\u671f')),
                ('user_title', models.CharField(default='', max_length=100)),
                ('content', models.CharField(default='', max_length=350)),
                ('isSubmit', models.BooleanField(default=False)),
                ('essay_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Essay')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User')),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
    ]
