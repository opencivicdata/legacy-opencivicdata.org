# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0008_auto_20140722_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpreadsheetMembership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('post_name', models.TextField()),
                ('role', models.TextField()),
                ('person', models.ForeignKey(to='upload.SpreadsheetPerson')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='spreadsheetperson',
            name='district',
        ),
        migrations.RemoveField(
            model_name='spreadsheetperson',
            name='position',
        ),
        migrations.AlterField(
            model_name='spreadsheetupload',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 9, 4, 13, 35, 9, 841327)),
        ),
    ]
