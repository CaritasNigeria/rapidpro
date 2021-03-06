# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-06 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0012_reset_3'),
        ('orgs', '0029_reset_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='org',
            field=models.ForeignKey(help_text='The organization this campaign exists for', on_delete=django.db.models.deletion.CASCADE, to='orgs.Org'),
        ),
    ]
