# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-27 09:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assets',
            options={'ordering': ['type', 'length']},
        ),
    ]