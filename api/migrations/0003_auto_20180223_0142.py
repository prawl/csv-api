# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-23 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180223_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importrow',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
