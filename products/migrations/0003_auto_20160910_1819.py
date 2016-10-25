# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 18:19
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('restaurants', '0002_restaurant_slug'),
        ('products', '0002_auto_20160910_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='consumableincome',
        ),
        migrations.RemoveField(
            model_name='order',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='consumableincome',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='consumableincome',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                    to='restaurants.Restaurant'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='remainingconsumable',
            unique_together=set([('restaurant', 'consumable')]),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]