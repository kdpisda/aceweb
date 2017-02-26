# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-20 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill_data',
            name='roll_no',
        ),
        migrations.AddField(
            model_name='student_data',
            name='skill',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='skill_data',
        ),
    ]