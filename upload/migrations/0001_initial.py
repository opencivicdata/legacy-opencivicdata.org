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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('district', models.TextField()),
                ('role', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpreadsheetPerson',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('url', models.TextField()),
                ('note', models.TextField()),
                ('person', models.ForeignKey(related_name='sources', to='upload.SpreadsheetPerson')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpreadsheetUpload',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2014, 9, 4, 21, 5, 32, 784195))),
                ('approved_by', models.ForeignKey(related_name='approvals', to=settings.AUTH_USER_MODEL, null=True)),
                ('jurisdiction', models.ForeignKey(related_name='uploads', to='opencivicdata.Jurisdiction', null=True)),
                ('rejected_by', models.ForeignKey(related_name='rejections', to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.ForeignKey(related_name='uploads', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpreadsheetUploadSource',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('url', models.TextField()),
                ('note', models.TextField()),
                ('upload', models.ForeignKey(related_name='sources', to='upload.SpreadsheetUpload')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='spreadsheetperson',
            name='spreadsheet',
            field=models.ForeignKey(related_name='people', to='upload.SpreadsheetUpload'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spreadsheetmembership',
            name='person',
            field=models.ForeignKey(related_name='memberships', to='upload.SpreadsheetPerson'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spreadsheetlink',
            name='person',
            field=models.ForeignKey(related_name='links', to='upload.SpreadsheetPerson'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spreadsheetcontactdetail',
            name='person',
            field=models.ForeignKey(related_name='contacts', to='upload.SpreadsheetPerson'),
            preserve_default=True,
        ),
    ]
