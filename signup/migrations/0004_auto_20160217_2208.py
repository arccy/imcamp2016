# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-17 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_auto_20160217_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='allergy',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='signup',
            name='group',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='signup',
            name='medical',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='signup',
            name='proof',
            field=models.FileField(blank=True, upload_to='uploads/proof/'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='special',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
