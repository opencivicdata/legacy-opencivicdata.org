# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_spreadsheetpersonsource'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpreadsheetUploadSource',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('upload', models.ForeignKey(to='upload.SpreadsheetUpload', to_field='id')),
                ('url', models.TextField()),
                ('note', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
