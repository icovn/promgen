# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 07:37


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promgen', '0010_auto_20161025_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exporter',
            name='path',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
