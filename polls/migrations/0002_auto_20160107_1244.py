# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-07 11:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='coice_text',
            new_name='choice_text',
        ),
    ]
