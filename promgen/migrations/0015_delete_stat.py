# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 08:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promgen', '0014_stat'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Stat',
        ),
    ]
