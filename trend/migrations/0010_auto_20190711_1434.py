# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-11 11:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0009_stream'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stream',
            name='user',
        ),
        migrations.DeleteModel(
            name='Stream',
        ),
    ]
