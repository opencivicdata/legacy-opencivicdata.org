# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_spreadsheetlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpreadsheetPersonSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('person', models.ForeignKey(to_field='id', to='upload.SpreadsheetPerson')),
                ('url', models.TextField()),
                ('note', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
