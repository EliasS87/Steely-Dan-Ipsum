# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-06 15:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0002_auto_20160906_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='number_of_paragraphs',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)]),
        ),
    ]
