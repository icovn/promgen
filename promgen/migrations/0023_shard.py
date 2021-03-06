# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 02:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def default_shard(apps, schema_editor):
    shard = apps.get_model('promgen', 'Shard')()
    shard.pk = 1
    shard.name = 'Default'
    shard.save()


class Migration(migrations.Migration):

    dependencies = [
        ('promgen', '0022_auto_20170116_0824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.RunPython(
            default_shard
        ),
        migrations.AddField(
            model_name='service',
            name='shard',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='promgen.Shard'),
            preserve_default=False,
        ),
    ]
