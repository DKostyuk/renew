# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-14 05:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180313_2121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='size_small',
            new_name='size',
        ),
    ]
