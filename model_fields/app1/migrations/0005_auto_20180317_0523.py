# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-17 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_withprimarykey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]