# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-23 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0002_auto_20160123_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]