from opencivicdata.models import Jurisdiction

from django import forms


class SpreadsheetUploadForm(forms.Form):
    jurisdiction = forms.ModelChoiceField(
        queryset=Jurisdiction.objects.all(),
        to_field_name="id"
    )
    source = forms.CharField()
    sheet = forms.FileField()
