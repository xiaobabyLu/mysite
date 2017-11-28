# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20171002_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
                ('user_type', models.CharField(choices=[('x1', 'xxx')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
