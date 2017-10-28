# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userchoice',
            name='browserFamily',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userchoice',
            name='browserVersion',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userchoice',
            name='deviceBrand',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userchoice',
            name='deviceFamily',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userchoice',
            name='deviceModel',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userchoice',
            name='deviceType',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userchoice',
            name='osFamily',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userchoice',
            name='osVersion',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
