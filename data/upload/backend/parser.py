import re
import csv
from data.upload.backend.xlrd import xlrd_dict_reader
from data.upload.backend.csv import csv_dict_reader
from data.upload.models import (SpreadsheetUpload, SpreadsheetPerson,
                                SpreadsheetContactDetail)

from contextlib import contextmanager
from pupa.scrape.helpers import Legislator
from pupa.scrape.popolo import Organization


OCD_SOURCE_URL = "http://opencivicdata.org/manual-data/source-notice"


def people_to_pupa(stream, transaction):
    org = Organization(
        name=transaction.jurisdiction.name,
        classification='legislature',
    )

    for row in stream:
        # XXX: Validate the row better.
        name = row.get("Name", "").strip()
        position = row.get("Position", "").strip()
        image = row.get("Image", None)

        if not name:
            raise ValueError("A name is required for each entry.")

        if not position:
            raise ValueError("A district is required for each entry.")

        obj = Legislator(name=name, district=position)
        if image:
            obj.image = image

        org.add_post(label=position, role="member")

        for key, keys in [
            ("email", ("Email 1", "Email 2", "Email 3")),
            ("address", ("Address 1", "Address 2", "Address 3")),
            ("voice", ("Phone 1", "Phone 2", "Phone 3")),
        ]:
            for k in keys:
                value = row.get(k)
                if value:
                    obj.add_contact_detail(type=key, value=value, note=k)

        obj.add_source(url=OCD_SOURCE_URL)
        obj.validate()
        obj.pre_save(transaction.jurisdiction.id)

        yield obj

        for related in obj._related:
            yield related

    for related in org._related:
        yield related
    yield org


def import_parsed_stream(stream, user, jurisdiction):
    upload = SpreadsheetUpload(user=user, jurisdiction=jurisdiction)
    upload.save()

    for person in stream:
        if (not person['District'] or not person['Name'] or
                not person['Position']):

            raise ValueError("Bad district or name")

        who = SpreadsheetPerson(
            name=person.pop('Name'),
            spreadsheet=upload,
            position=person.pop('Position'),
            district=person.pop('District'),
        )
        who.save()

        contact_details = [
            "Address", "Phone", "Email", "Fax", "Cell",
            "Twitter", "Facebook",
        ]
        links = ["Website", "Homepage"]
        sources = ["Source"]

        for key, value in person.items():
            match = re.match("(?P<key>) \((?P<label>.*\))?", key)
            print(match)

        #    for index in indexes:
        #        value = person.get(index)
        #        if value:
        #            a = SpreadsheetContactDetail(
        #                person=who,
        #                type=type,
        #                value=value,
        #                label=index,
        #                note="Imported by data.upload",
        #            )
        #            a.save()

    return upload


def import_stream(stream, extension, user, jurisdiction):
    reader = {"csv": csv_dict_reader,
              "xlsx": xlrd_dict_reader,
              "xls": xlrd_dict_reader}[extension]

    return import_parsed_stream(reader(stream), user, jurisdiction)


@contextmanager
def import_file_stream(fpath, user, jurisdiction):
    _, xtn = fpath.rsplit(".", 1)

    with open(fpath, 'br') as fd:
        yield import_stream(fd, xtn, user, jurisdiction)
