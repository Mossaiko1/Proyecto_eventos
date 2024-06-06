from django.urls import path
from .views import view_event

urlpatterns= [
    path('', view_event, name ='eventos'),
]