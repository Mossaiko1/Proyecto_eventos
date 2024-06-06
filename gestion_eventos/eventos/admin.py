from django.contrib import admin
from .models import Participant
from .models import Event

admin.site.register(Event)
admin.site.register(Participant)