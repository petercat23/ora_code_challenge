# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='user12345', max_length=256),
            preserve_default=False,
        ),
    ]