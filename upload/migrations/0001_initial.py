# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opencivicdata', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpreadsheetUpload',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', null=True)),
                ('approved_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', null=True)),
                ('rejected_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', null=True)),
                ('jurisdiction', models.ForeignKey(to='opencivicdata.Jurisdiction', to_field='id', null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2014, 5, 27, 18, 36, 36, 34501))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
