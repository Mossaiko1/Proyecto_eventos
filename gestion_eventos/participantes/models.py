from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    status = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.name}{self.last_name}"