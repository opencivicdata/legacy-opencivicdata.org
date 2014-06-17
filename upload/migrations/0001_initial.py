# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('opencivicdata', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SpreadsheetUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, to_field='id')),
                ('approved_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, to_field='id')),
                ('rejected_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, to_field='id')),
                ('jurisdiction', models.ForeignKey(to='opencivicdata.Jurisdiction', null=True, to_field='id')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2014, 6, 17, 17, 55, 59, 503641))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
