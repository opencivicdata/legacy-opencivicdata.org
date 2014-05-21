import datetime as dt
from collections import defaultdict

from django.db import models
from django.contrib.auth.models import User

from opencivicdata.models.jurisdiction import Jurisdiction


class SpreadsheetUpload(models.Model):
    user = models.ForeignKey(User, related_name='uploads', null=True)
    approved_by = models.ForeignKey(User, related_name='approvals', null=True)
    rejected_by = models.ForeignKey(User, related_name='rejections', null=True)
    jurisdiction = models.ForeignKey(
        Jurisdiction,
        related_name='uploads',
        null=True,  # If it's Null, then we know that we need to
        # do a match against the jurisdiction we need.
    )
    created_at = models.DateTimeField(default=dt.datetime.utcnow())

    def is_actionable(self):
        return ((self.approved_by is None) and (self.rejected_by is None))


class SpreadsheetPerson(models.Model):
    name = models.TextField()
    image = models.TextField()
    party = models.TextField(blank=True)
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
