# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 13:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20170917_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forumpost',
            old_name='userp',
            new_name='author',
        ),
    ]
