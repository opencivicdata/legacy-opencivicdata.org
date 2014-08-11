# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0007_auto_20140717_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spreadsheetperson',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='spreadsheetperson',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='spreadsheetupload',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 7, 22, 14, 45, 58, 697944)),
        ),
    ]
