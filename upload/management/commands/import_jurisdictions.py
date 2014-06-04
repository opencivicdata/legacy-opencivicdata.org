import csv
from opencivicdata.models import Jurisdiction, Division

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    args = '<csv_mapping>'
    help = 'Load in Jurisdictions'

    def load_csv(self, file_):
        seen = set()

        with open(file_, 'r') as fd:
            stream = csv.DictReader(fd)
            for entry in stream:
                jurisdiction = entry['jurisdiction']
                if jurisdiction in seen:
                    raise ValueError(
                        "Two of the same jurisdiction, likely bad data."
                        + " Bad ID: '%s'" % (jurisdiction)
                    )
                seen.add(jurisdiction)

                division = Division.objects.get(id=entry['division'])
                try:
                    print(entry)
                    jurisdiction = Jurisdiction.objects.get(
                        id=entry['jurisdiction']
                    )
                except Jurisdiction.DoesNotExist:
                    jurisdiction = Jurisdiction()

                jurisdiction.id = entry['jurisdiction']
                jurisdiction.division = division
                jurisdiction.name = entry['name']
                jurisdiction.save()

                print(jurisdiction)

    def handle(self, *args, **options):
        for csv_file in args:
            print(self.load_csv(csv_file))
