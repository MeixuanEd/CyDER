# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='config',
            field=models.TextField(default='null'),
        ),
    ]
