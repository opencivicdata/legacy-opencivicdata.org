# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_spreadsheetuploadsource'),
    ]

    operations = [
        migrations.AddField(
            model_name='spreadsheetperson',
            name='end_date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spreadsheetperson',
            name='start_date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='spreadsheetupload',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 7, 17, 21, 21, 37, 175972)),
        ),
    ]
