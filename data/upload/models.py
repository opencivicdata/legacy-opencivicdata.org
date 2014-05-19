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
    position = models.TextField()
    spreadsheet = models.ForeignKey(SpreadsheetUpload, related_name='people')
    code = models.TextField()
    # HStore here.

    def as_csv_dict(self):
        row = {"Name": self.name, "Position": self.position,}
        if self.code:
            row['Code'] = self.code

        types = defaultdict(lambda: 1)

        for contact in self.contacts.all():
            class_, _ = contact.label.split(" ", 1)
            slug = "%s %s" % ({
                "address": "Address",
                "voice": "Phone",
                "email": "Email",
            }[contact.type], types[contact.label])
            types[contact.type] += 1
            row[slug] = contact.value

        return row


class SpreadsheetContactDetail(models.Model):
    person = models.ForeignKey(
        SpreadsheetPerson,
        related_name='contacts'
    )
    type = models.TextField()
    value = models.TextField()
    label = models.TextField()
    note = models.TextField()
