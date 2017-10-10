# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 04:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0006_auto_20170825_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='group_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to='snippets.Group'),
        ),
    ]
