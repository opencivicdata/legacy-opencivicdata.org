import datetime as dt
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
    district = models.TextField()
    spreadsheet = models.ForeignKey(SpreadsheetUpload, related_name='people')
    # HStore here.

    def as_dict(self):
        row = {"Name": self.name, "District": self.district,}

        for i, address in enumerate(self.addresses.all(), start=1):
            row['Address {}'.format(i)] = address.address

        for i, phone in enumerate(self.phones.all(), start=1):
            row['Phone {}'.format(i)] = phone.phone

        for i, email in enumerate(self.emails.all(), start=1):
            row['Email {}'.format(i)] = email.email

        return row


class SpreadsheetAddress(models.Model):
    person = models.ForeignKey(SpreadsheetPerson, related_name='addresses')
    address = models.TextField()


class SpreadsheetPhone(models.Model):
    person = models.ForeignKey(SpreadsheetPerson, related_name='phones')
    phone = models.TextField()


class SpreadsheetEmail(models.Model):
    person = models.ForeignKey(SpreadsheetPerson, related_name='emails')
    email = models.TextField()
