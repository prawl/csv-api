# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-24 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180224_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importrow',
            name='date',
            field=models.DateTimeField(verbose_name=['%m/%d/%Y']),
        ),
    ]
