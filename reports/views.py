from collections import OrderedDict

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Max

from pupa.models import RunPlan, DataQualityChecks


@login_required
def report(request):
    # Identify the most recent plans for each jurisdiction
    newest_plans_by_jurisdiction = RunPlan.objects.values('jurisdiction').annotate(newest_plan=Max('id')).values_list('newest_plan', flat=True)

    # Identify all checks that have been run in any of these reports
    newest_checks_by_jurisdiction = DataQualityChecks.objects.filter(plan__id__in=newest_plans_by_jurisdiction)
    all_checks = set([(x.type.object_type, x.type.name) for x in newest_checks_by_jurisdiction])
    all_checks = sorted(sorted(all_checks, key=lambda x: x[1]), key=lambda x: x[0])

    # Split the checks into categories by jurisdiction and object type
    checks_by_jurisdiction = {}

    for jurisdiction in newest_plans_by_jurisdiction:
        checks = DataQualityChecks.objects.filter(plan__id=jurisdiction)

        # Initialize all checks, in case divisions differ in which they use
        checks_by_type = OrderedDict()
        for check in all_checks:
            if check[0] not in checks_by_type:
                checks_by_type[check[0]] = OrderedDict()
            checks_by_type[check[0]][check[1]] = None

        for check in checks:
            bad_cell = (check.value > check.type.bad_range)
            # Assume that checks values are either percentages or counts
            if check.type.is_percentage:
                value = str(int(check.value)) + "%"
            else:
                value = str(int(check.value))
            checks_by_type[check.type.object_type][check.type.name] = (value, bad_cell)

        jurisdiction_name = RunPlan.objects.get(id=jurisdiction).jurisdiction
        checks_by_jurisdiction[jurisdiction_name] = checks_by_type

    object_types = OrderedDict()
    for check in all_checks:
        object_types[check[0]] = object_types.get(check[0], 0) + 1

    return render(request, "data/reports/reports.html", {
        "object_types": object_types,
        "checks": [x[1] for x in all_checks],
        "checks_by_jurisdiction": checks_by_jurisdiction,
    })
