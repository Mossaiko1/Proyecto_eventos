from django import forms
from .models import Event

class FormEvent(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name_event', 'description', 'date', 'time', 'location']