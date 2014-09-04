# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0002_auto_20140904_1357'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SpreadsheetContactDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('type', models.TextField()),
                ('value', models.TextField()),
                ('label', models.TextField()),
                ('note', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpreadsheetLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('url', models.TextField()),
                ('note', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpreadsheetMembership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('post_name', models.TextField()),
                ('role', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpreadsheetPerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.TextField()),
                ('image', models.TextField()),
                ('party', models.TextField(blank=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('code', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpreadsheetPersonSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('url', models.TextField()),
                ('note', models.TextField()),
                ('person', models.ForeignKey(to='upload.SpreadsheetPerson', related_name='sources')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpreadsheetUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2014, 9, 4, 13, 57, 51, 17428))),
                ('approved_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='approvals', null=True)),
                ('jurisdiction', models.ForeignKey(to='opencivicdata.Jurisdiction', related_name='uploads', null=True)),
                ('rejected_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='rejections', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='uploads', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpreadsheetUploadSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('url', models.TextField()),
                ('note', models.TextField()),
                ('upload', models.ForeignKey(to='upload.SpreadsheetUpload', related_name='sources')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='spreadsheetperson',
            name='spreadsheet',
            field=models.ForeignKey(to='upload.SpreadsheetUpload', related_name='people'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spreadsheetmembership',
            name='person',
            field=models.ForeignKey(to='upload.SpreadsheetPerson', related_name='memberships'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spreadsheetlink',
            name='person',
            field=models.ForeignKey(to='upload.SpreadsheetPerson', related_name='links'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spreadsheetcontactdetail',
            name='person',
            field=models.ForeignKey(to='upload.SpreadsheetPerson', related_name='contacts'),
            preserve_default=True,
        ),
    ]
