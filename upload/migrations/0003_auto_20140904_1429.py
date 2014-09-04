# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20140904_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spreadsheetmembership',
            old_name='post_name',
            new_name='district',
        ),
        migrations.AlterField(
            model_name='spreadsheetupload',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 4, 14, 29, 25, 913118)),
        ),
    ]
