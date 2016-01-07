# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-07 22:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='World',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('world_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TextEntry',
            fields=[
                ('variable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='worldbuilder.Variable')),
            ],
            bases=('worldbuilder.variable',),
        ),
        migrations.AddField(
            model_name='variable',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldbuilder.Entry'),
        ),
        migrations.AddField(
            model_name='entry',
            name='world',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worldbuilder.World'),
        ),
    ]