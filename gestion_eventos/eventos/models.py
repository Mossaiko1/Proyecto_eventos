from django.db import models
from participantes.models import Participant

class Event(models.Model):
    name_event = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name_event
    

class Attendance(models.Model):
    event = models.ManyToManyField(Event)
    participant = models.ManyToManyField(Participant)

    def __str__(self):
        return f"Asistencia de {self.participant.name} a {self.event.name_event}"
