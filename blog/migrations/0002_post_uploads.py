# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-20 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='uploads',
            field=models.ImageField(blank=True, upload_to=b'uploads/'),
        ),
    ]
