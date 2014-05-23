import csv
from opencivicdata.models import Jurisdiction, Division

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = '<csv_mapping>'
    help = 'Load in Jurisdictions'

    def load_csv(self, file_):
        with open(file_, 'r') as fd:
            stream = csv.DictReader(fd)
            for entry in stream:
                division = Division.objects.get(id=entry['division'])
                jurisdiction = Jurisdiction.objects.create(
                    id=entry['jurisidiction'],
                    division=division,
                    name=entry['name']
                )
                print(jurisdiction)

    def handle(self, *args, **options):
        for csv_file in args:
            print(self.load_csv(csv_file))
