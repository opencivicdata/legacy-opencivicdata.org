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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
