import re
import csv
from data.upload.backend.xlrd import xlrd_dict_reader
from data.upload.backend.csv import csv_dict_reader
from data.upload.models import (SpreadsheetUpload, SpreadsheetPerson,
                                SpreadsheetUploadSource, SpreadsheetPersonSource,
                                SpreadsheetLink, SpreadsheetContactDetail)

from contextlib import contextmanager
from pupa.scrape.helpers import Legislator
from pupa.scrape.popolo import Organization


OCD_SOURCE_URL = "http://opencivicdata.org/manual-data/source-notice"


def people_to_pupa(stream, transaction):
    org = Organization(
        name=transaction.jurisdiction.name,
        classification='legislature',
    )

    for person in stream:
        name = person.name
        position = person.position
        district = person.district
        image = person.image

        if not name or not district:
            raise ValueError("A name and district is required for each entry.")

        if position is None:
            position = "member"

        obj = Legislator(name=name, district=district)

        if image:
            obj.image = image

        org.add_post(label="%s, %s" % (position, district), role=position)

        for detail in person.contacts.all():
            obj.add_contact_detail(
                type=detail.type,
                value=detail.value,
                note=detail.note,
            )

        for link in person.links.all():
            obj.add_link(
                url=link.url,
                note=link.url
            )

        for source in (list(person.sources.all())
                       + list(transaction.sources.all())):
            obj.add_source(
                url=source.url,
                note=source.note,
            )

        obj.validate()
        obj.pre_save(transaction.jurisdiction.id)

        yield obj

        for related in obj._related:
            yield related

    for related in org._related:
        yield related
    yield org


def import_parsed_stream(stream, user, jurisdiction, sources):
    upload = SpreadsheetUpload(user=user, jurisdiction=jurisdiction)
    upload.save()

    for source in sources:
        a = SpreadsheetUploadSource(
            upload=upload,
            url=source,
            note="Default Spreadsheet Source"
        )
        a.save()


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
        if 'Image' in person:
            who.image = person.pop("Image")
        who.save()

        contact_details = {
            "Address": "address",
            "Phone": "voice",
            "Email": "email",
            "Fax": "fax",
            "Cell": "voice",
            "Twitter": "twitter",
            "Facebook": "facebook"
        }
        links = ["Website", "Homepage"]
        sources = ["Source"]

        for key, value in person.items():
            match = re.match("(?P<key>.*) (?P<label>\(.*\))?", key)
            root = key
            label = None
            if match:
                d = match.groupdict()
                root = d['key']
                label = d['label'].rstrip(")").lstrip("(")

            if root in sources:
                a = SpreadsheetPersonSource(
                    person=who,
                    url=value,
                    note=key
                )
                a.save()
                continue

            # If we've got a link.
            if root in links:
                a = SpreadsheetLink(
                    person=who,
                    url=value,
                    note=key,
                )
                a.save()
                continue

            # If we've got a contact detail.
            if root in contact_details:
                type_ = contact_details[root]
                a = SpreadsheetContactDetail(
                    person=who,
                    type=type_,
                    value=value,
                    label=label or "",
                    note=key,
                )
                a.save()
                continue

            raise ValueError("Unknown spreadhseet key: %s" % (key))


    return upload


def import_stream(stream, extension, user, jurisdiction, sources):
    reader = {"csv": csv_dict_reader,
              "xlsx": xlrd_dict_reader,
              "xls": xlrd_dict_reader}[extension]

    return import_parsed_stream(reader(stream), user, jurisdiction, sources)


@contextmanager
def import_file_stream(fpath, user, jurisdiction, sources):
    _, xtn = fpath.rsplit(".", 1)

    with open(fpath, 'br') as fd:
        yield import_stream(fd, xtn, user, jurisdiction, sources)
