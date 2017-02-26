# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-20 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumni_data',
            old_name='enroll_no',
            new_name='roll_no',
        ),
        migrations.AddField(
            model_name='alumni_data',
            name='photo',
            field=models.ImageField(default='default.png', upload_to='faculty_images/'),
        ),
        migrations.AlterField(
            model_name='alumni_data',
            name='other',
            field=tinymce.models.HTMLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]