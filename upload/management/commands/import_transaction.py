import csv
from django.contrib.auth.models import User
from opencivicdata.models import Jurisdiction, Division
from upload.backend.parser import import_stream, people_to_pupa
from upload.backend.importer import do_import
from upload.models import SpreadsheetUpload

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = '<transaction> <user>'
    help = 'Import a Sheet'

    def import_transaction(self, transaction_id, username):
        user = User.objects.get(username=username)
        transaction = SpreadsheetUpload.objects.get(id=transaction_id)

        assert transaction.approved_by is None

        stream = people_to_pupa(transaction.people.all(), transaction)
        report = do_import(stream, transaction)
        transaction.approved_by = user
        transaction.save()

    def handle(self, *args, **options):
        return self.import_transaction(*args)
