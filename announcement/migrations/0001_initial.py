# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-20 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='announcement_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('content', models.CharField(blank=True, max_length=120, null=True)),
                ('issuer', models.CharField(blank=True, max_length=120, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='resources/')),
                ('date_issued', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(default=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
