# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_spreadsheetperson'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpreadsheetContactDetail',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('person', models.ForeignKey(to='upload.SpreadsheetPerson', to_field='id')),
                ('type', models.TextField()),
                ('value', models.TextField()),
                ('label', models.TextField()),
                ('note', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
