from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings

from .backend.parser import import_stream, people_to_pupa
from .backend.importer import do_import
from .forms import SpreadsheetUploadForm
from .models import SpreadsheetUpload
from opencivicdata.models import Jurisdiction

import json


@login_required
def home(request):
    if request.method == 'POST':
        form = SpreadsheetUploadForm(request.POST, request.FILES)
        if form.is_valid():
            return upload(request)
    else:
        form = SpreadsheetUploadForm()

    user = request.user
    if user.is_anonymous():
        user = None

    return render(request, 'data/upload/public/index.html', {
        "form": form,
        "user": user,
    })


    jurisdictions = Jurisdiction.objects.all()
    return render(request, "data/upload/public/index.html", {
        "jurisdictions": jurisdictions,
        "user": user,
    })


@require_http_methods(["POST"])
@login_required
def upload(request):
    try:
        jurisdiction = Jurisdiction.objects.get(id=request.POST['jurisdiction'])
    except Jurisdiction.DoesNotExist as e:
        return render(request, "data/upload/public/upload_fail.html", {
            "exception": e,
            "jurisdiction": request.POST['jurisdiction'],
            "admins": settings.ADMINS,
        })

    sheet = request.FILES['sheet']
    _, xtn = sheet.name.rsplit(".", 1)
    sources = [
        request.POST['source']
        # XXX: Allow a list here.
    ]

    user = request.user
    if user.is_anonymous():
        user = None

    try:
        transaction = import_stream(
            sheet.read(),
            xtn,
            user,
            jurisdiction,
            sources,
        )
    except ValueError as e:
        return render(request, "data/upload/public/upload_fail.html", {
            "exception": e,
            "jurisdiction": request.POST['jurisdiction'],
            "admins": settings.ADMINS,
        })

    return redirect('manage', transaction.id)


def guide(request):
    return render(request, "data/upload/public/guide.html", {})


@login_required
def queue(request):
    return render(request, "data/upload/public/queue.html", {
        "uploads": SpreadsheetUpload.objects.filter(
            approved_by__isnull=True,
            rejected_by__isnull=True,
        ).all()
    })


def manage(request, transaction):
    transaction = SpreadsheetUpload.objects.get(id=int(transaction))

    return render(request, "data/upload/public/manage.html", {
        "transaction": transaction,
        "user": request.user,
    })


@staff_member_required
@require_http_methods(["POST"])
def migrate(request):
    transaction_id = int(request.POST['transaction'])
    transaction = SpreadsheetUpload.objects.get(id=transaction_id)

    reject = False
    if 'reject' in request.POST:
        reject = True

    if not transaction.is_actionable():
        return render(request, "data/upload/public/migrate_fail.html", {
            "transaction": transaction,
            "admins": settings.ADMINS,
        })

    if reject:
        transaction.rejected_by = request.user
        transaction.save()
        return redirect('manage', transaction.id)
    else:
        stream = people_to_pupa(transaction.people.all(), transaction)
        report = do_import(stream, transaction)
        transaction.approved_by = request.user
        transaction.save()

        return render(request, "data/upload/public/migrate.html", {
            "transaction": transaction,
            "report": report,
            "report_pretty": json.dumps(report, indent=4),
        })
