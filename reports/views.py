from collections import OrderedDict

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Max

from pupa.models import RunPlan, DataQualityChecks


@login_required
def report(request):
    # Identify the most recent plans for each jurisdiction
    newest_plans_by_jurisdiction = RunPlan.objects.values('jurisdiction').annotate(newest_plan=Max('id')).values_list('newest_plan', flat=True)

    # Identify all measures that have been run in any of these reports
    newest_measures_by_jurisdiction = DataQualityChecks.objects.filter(plan__id__in=newest_plans_by_jurisdiction)
    all_measures = set([(x.type.object_type, x.type.name) for x in newest_measures_by_jurisdiction])
    all_measures = sorted(sorted(all_measures, key=lambda x: x[1]), key=lambda x: x[0])

    # Split the measures into categories by jurisdiction and object type
    measures_by_jurisdiction = {}

    for jurisdiction in newest_plans_by_jurisdiction:
        measures = DataQualityChecks.objects.filter(plan__id=jurisdiction)

        # Initialize all measures, in case divisions differ in which they use
        measures_by_type = OrderedDict()
        for measure in all_measures:
            if measure[0] not in measures_by_type:
                measures_by_type[measure[0]] = OrderedDict()
            measures_by_type[measure[0]][measure[1]] = None

        for measure in measures:
            measures_by_type[measure.type.object_type][measure.type.name] = measure.value

        jurisdiction_name = RunPlan.objects.get(id=jurisdiction).jurisdiction
        measures_by_jurisdiction[jurisdiction_name] = measures_by_type

    object_types = OrderedDict()
    for measure in all_measures:
        object_types[measure[0]] = object_types.get(measure[0], 0) + 1

    return render(request, "data/reports/reports.html", {
        "object_types": object_types,
        "measures": [x[1] for x in all_measures],
        "measures_by_jurisdiction": measures_by_jurisdiction,
    })
