from opencivicdata.models import Jurisdiction

from django.template import Context
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from django.forms import widgets
from django import forms


class Select2Widget(widgets.TextInput):
    def render(self, name, value, attrs=None):
        return mark_safe(get_template(
            'data/upload/forms/select2.html'
        ).render(Context({
            "name": name,
            "value": value,
        })))


class JurisdictionModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.id


class SpreadsheetUploadForm(forms.Form):
    jurisdiction = JurisdictionModelChoiceField(
        empty_label=None,
        queryset=Jurisdiction.objects.all(),
        widget=Select2Widget,
    )
    source = forms.CharField()
    sheet = forms.FileField()
