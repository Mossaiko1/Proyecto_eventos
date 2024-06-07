from django.db import models

class Participant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    status = models.BooleanField(default=True)
    
    
    event = models.ForeignKey('eventos.Event', on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.first_name} {self.last_name}'