# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-29 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_auto_20160312_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='gender',
            field=models.CharField(choices=[('M', '男'), ('F', '女'), ('O', '其他')], max_length=1),
        ),
    ]