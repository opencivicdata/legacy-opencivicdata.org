#

import xlrd
from pupa.scrape.popolo import Person, Organization, Membership


OCD_SOURCE_URL = "http://opencivicdata.org/manual-data/source-notice"


def xlrd_dict_reader(stream):
    book = xlrd.open_workbook(file_contents=stream)
    sheet = book.sheets()[0]  # XXX: Fix this

    rows = iter([sheet.row(x) for x in range(sheet.nrows)])
    header = next(rows)
    for row in rows:
        yield dict(zip([x.value for x in header],
                       [x.value for x in row]))
