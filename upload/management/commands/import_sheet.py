import csv
from django.contrib.auth.models import User
from opencivicdata.models import Jurisdiction, Division
from upload.backend.parser import import_stream
from django.core.management import call_command

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = '<csv> <jurisdiction> <source> <user> <import>'
    help = 'Load in Sheets'

    def load_csv(self, file_, jurisdiction_id, source, username, do_import="False"):
        user = User.objects.get(username=username)
        do_import = do_import.lower() == "true"

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

        if do_import:
            call_command(
                'import_transaction',
                transaction.id,
                user.username,
            )

    def handle(self, *args, **options):
        return self.load_csv(*args)
