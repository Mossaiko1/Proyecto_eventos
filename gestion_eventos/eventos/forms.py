from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name_event', 'date', 'time', 'location', 'description', 'capacity']
        labels = {
            'name_event': 'Nombre del evento',
            'date': 'Fecha',
            'time': 'Hora',
            'location': 'Ubicación',
            'description': 'Descripción',
            'capacity': 'Capacidad',
        }
        widgets = {
            'name_event': forms.TextInput(attrs={'placeholder': 'Nombre del evento', 'class': 'form-control'}),
            'date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'placeholder': 'HH:MM', 'class': 'form-control', 'type': 'time'}),
            'location': forms.TextInput(attrs={'placeholder': 'Ubicación', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Descripción', 'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'placeholder': 'Capacidad', 'class': 'form-control'}),
        }
