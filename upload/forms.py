from opencivicdata.models import Jurisdiction

from django import forms


class JurisdictionModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.id


class SpreadsheetUploadForm(forms.Form):
    jurisdiction = JurisdictionModelChoiceField(
        empty_label=None,
        queryset=Jurisdiction.objects.all(),
    )
    source = forms.CharField()
    sheet = forms.FileField()
