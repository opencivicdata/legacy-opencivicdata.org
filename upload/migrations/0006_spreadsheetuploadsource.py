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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('upload', models.ForeignKey(to_field='id', to='upload.SpreadsheetUpload')),
                ('url', models.TextField()),
                ('note', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
