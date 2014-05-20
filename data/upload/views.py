from django.shortcuts import render_to_response
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from data.upload.backend.parser import import_stream, people_to_pupa
from data.upload.backend.importer import do_import
from data.upload.models import SpreadsheetUpload
from opencivicdata.models import Jurisdiction


@login_required
def home(request):
    return render_to_response("data/upload/public/index.html", {})


@login_required
def queue(request):
    return render_to_response("data/upload/public/queue.html", {
        "uploads": SpreadsheetUpload.objects.filter(
            approved_by__isnull=True
        ).all()
    })


@login_required
@require_http_methods(["POST"])
def upload(request):
    try:
        jurisdiction = Jurisdiction.objects.get(id=request.POST['jurisdiction'])
    except Jurisdiction.DoesNotExist as e:
        return render_to_response("data/upload/public/upload_fail.html", {
            "exception": e,
            "jurisdiction": request.POST['jurisdiction']
        })

    sheet = request.FILES['sheet']
    _, xtn = sheet.name.rsplit(".", 1)


    try:
        transaction = import_stream(
            sheet.read(),
            xtn,
            request.user,
            jurisdiction,
        )
    except ValueError as e:
        return render_to_response("data/upload/public/upload_fail.html", {
            "exception": e,
            "jurisdiction": request.POST['jurisdiction']
        })



    return render_to_response("data/upload/public/upload.html", {
        "transaction": transaction,
    })


@staff_member_required
def manage(request, transaction):
    transaction = SpreadsheetUpload.objects.get(id=int(transaction))

    return render_to_response("data/upload/public/manage.html", {
        "transaction": transaction,
    })


@staff_member_required
@require_http_methods(["POST"])
def migrate(request):
    transaction_id = int(request.POST['transaction'])
    transaction = SpreadsheetUpload.objects.get(id=transaction_id)

    if transaction.approved_by:
        return render_to_response("data/upload/public/migrate_fail.html", {
            "transaction": transaction,
        })

    approver = request.user

    def migrate_spreadsheet(transaction):
        for person in transaction.people.all():
            yield person.as_csv_dict()

    stream = people_to_pupa(migrate_spreadsheet(transaction), transaction)
    report = do_import(stream, transaction)

    transaction.approved_by = approver
    transaction.save()

    return render_to_response("data/upload/public/migrate.html", {
        "transaction": transaction,
        "report": report,
    })
