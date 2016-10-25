# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 12:12
from __future__ import unicode_literals

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0004_auto_20160910_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='consumables',
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.ManyToManyField(related_name='fukk', to='products.Quantity'),
        ),
        migrations.AlterField(
            model_name='checkoutproduct',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 11, 12, 12, 54, 764682)),
        ),
        migrations.AlterField(
            model_name='consumableincome',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 11, 12, 12, 54, 764142)),
        ),
        migrations.AlterField(
            model_name='quantity',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dfadsd',
                                    to='products.Product'),
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 11, 12, 12, 54, 766565)),
        ),
    ]
