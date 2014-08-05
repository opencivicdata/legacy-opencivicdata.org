from pupa.scrape import (Jurisdiction, Person, Organization, Membership, Post)
from pupa.importers import (OrganizationImporter, PersonImporter, PostImporter,
                            MembershipImporter)
from django.db import transaction


def do_import(stream, stransaction):
    stream = list(stream)
    jurisdiction_id = stransaction.jurisdiction.id

    org_importer = OrganizationImporter(jurisdiction_id)
    person_importer = PersonImporter(jurisdiction_id)
    post_importer = PostImporter(jurisdiction_id, org_importer)
    membership_importer = MembershipImporter(
        jurisdiction_id,
        person_importer,
        org_importer,
        post_importer
    )

    report = {}

    def tfilter(otype, stream):
        for el in filter(lambda x: isinstance(x, otype), stream):
            yield el.as_dict()

    with transaction.atomic():
        report.update(org_importer.import_data(tfilter(Organization, stream)))
        report.update(person_importer.import_data(tfilter(Person, stream)))
        report.update(post_importer.import_data(tfilter(Post, stream)))
        report.update(membership_importer.import_data(
            tfilter(Membership, stream)))

    return report
