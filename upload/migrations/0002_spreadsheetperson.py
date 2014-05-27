# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpreadsheetPerson',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('image', models.TextField()),
                ('party', models.TextField(blank=True)),
                ('position', models.TextField()),
                ('district', models.TextField()),
                ('spreadsheet', models.ForeignKey(to='upload.SpreadsheetUpload', to_field='id')),
                ('code', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
