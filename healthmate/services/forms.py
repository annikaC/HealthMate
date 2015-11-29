from django import forms

from leaflet.forms.widgets import LeafletWidget

from models import Service


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ('name', 'categories', 'location')
        widgets = {'location': LeafletWidget()}
