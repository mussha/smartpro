# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 10:02
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0012_auto_20161017_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutproduct',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='consumableincome',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reportconsmable',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
