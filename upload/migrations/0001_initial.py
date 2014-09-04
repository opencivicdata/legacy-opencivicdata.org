# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SpreadsheetContactDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
        migrations.AddField(
            model_name='spreadsheetmembership',
            name='person',
            field=models.ForeignKey(to='upload.SpreadsheetPerson'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spreadsheetlink',
            name='person',
            field=models.ForeignKey(to='upload.SpreadsheetPerson'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spreadsheetcontactdetail',
            name='person',
            field=models.ForeignKey(to='upload.SpreadsheetPerson'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='SpreadsheetPersonSource',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('url', models.TextField()),
                ('note', models.TextField()),
                ('person', models.ForeignKey(to='upload.SpreadsheetPerson')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpreadsheetUpload',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2014, 9, 4, 13, 50, 6, 62194))),
                ('approved_by', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
                ('jurisdiction', models.ForeignKey(null=True, to='opencivicdata.Jurisdiction')),
                ('rejected_by', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='spreadsheetperson',
            name='spreadsheet',
            field=models.ForeignKey(to='upload.SpreadsheetUpload'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='SpreadsheetUploadSource',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('url', models.TextField()),
                ('note', models.TextField()),
                ('upload', models.ForeignKey(to='upload.SpreadsheetUpload')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
