# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-12 05:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='doc_url',
        ),
    ]