# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-14 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0011_delete_neighbourhood'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighbourhood', models.CharField(max_length=100)),
                ('neighbourhood_location', models.CharField(max_length=100)),
                ('occupants_count', models.IntegerField()),
            ],
        ),
    ]
