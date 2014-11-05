# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spreadsheetperson',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='spreadsheetperson',
            name='start_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='spreadsheetupload',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 5, 15, 27, 55, 589233)),
        ),
    ]
