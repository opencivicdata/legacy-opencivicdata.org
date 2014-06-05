# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_spreadsheetuploadsource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spreadsheetupload',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 6, 5, 17, 18, 33, 707779)),
        ),
    ]
