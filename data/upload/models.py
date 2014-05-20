import datetime as dt
from collections import defaultdict

from django.db import models
from django.contrib.auth.models import User

from opencivicdata.models.jurisdiction import Jurisdiction


class SpreadsheetUpload(models.Model):
    user = models.ForeignKey(User, related_name='uploads')
    approved_by = models.ForeignKey(User, related_name='approvals', null=True)
    jurisdiction = models.ForeignKey(
        Jurisdiction,
        related_name='uploads'
    )
    created_at = models.DateTimeField(default=dt.datetime.utcnow())


class SpreadsheetPerson(models.Model):
    name = models.TextField()
    image = models.TextField()
    position = models.TextField()
    district = models.TextField()
    spreadsheet = models.ForeignKey(SpreadsheetUpload, related_name='people')
    code = models.TextField()
    # HStore here.


class SpreadsheetContactDetail(models.Model):
    person = models.ForeignKey(
        SpreadsheetPerson,
        related_name='contacts'
    )
    type = models.TextField()
    value = models.TextField()
    label = models.TextField()
    note = models.TextField()


class SpreadsheetLink(models.Model):
    person = models.ForeignKey(
        SpreadsheetPerson,
        related_name='links'
    )
    url = models.TextField()
    note = models.TextField()


class SpreadsheetPersonSource(models.Model):
    person = models.ForeignKey(
        SpreadsheetPerson,
        related_name='sources'
    )
    url = models.TextField()
    note = models.TextField()


class SpreadsheetUploadSource(models.Model):
    upload = models.ForeignKey(
        SpreadsheetUpload,
        related_name='sources'
    )
    url = models.TextField()
    note = models.TextField()
