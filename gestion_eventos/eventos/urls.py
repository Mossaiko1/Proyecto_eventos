from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('eventos/confirm_delete/<int:event_id>/', views.confirm_delete_event, name='confirm_delete_event'),
    path('eventos/eliminar/<int:pk>/', views.confirm_delete_event, name='confirm_delete_event'),
    
]
