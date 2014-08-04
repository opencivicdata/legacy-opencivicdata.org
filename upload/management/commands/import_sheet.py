import csv
from django.contrib.auth.models import User
from opencivicdata.models import Jurisdiction, Division
from upload.backend.parser import import_stream

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = '<csv> <jurisdiction> <source> <user>'
    help = 'Load in Sheets'

    def load_csv(self, file_, jurisdiction_id, source, username):

        user = User.objects.get(username=username)

        jurisdiction = Jurisdiction.objects.get(id=jurisdiction_id)
        _, xtn = file_.rsplit(".", 1)

        sources = [source,]

        with open(file_, 'rb') as fd:
            transaction = import_stream(
                fd.read(),
                xtn,
                user,
                jurisdiction,
                sources,
            )

    def handle(self, *args, **options):
        return self.load_csv(*args)
