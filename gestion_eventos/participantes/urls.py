from django.urls import path
from .views import participant_list, edit_participant, confirm_delete_participant, delete_participant, change_status

urlpatterns = [
    path('', participant_list, name='participant_list'),
    path('editar/<int:participant_id>/', edit_participant, name='edit_participant'),
    path('eliminar/<int:participant_id>/', confirm_delete_participant, name='confirm_delete_participant'),
    path('eliminar-confirmado/<int:participant_id>/', delete_participant, name='delete_participant'),
    path('cambiar_estado/', change_status, name='change_status'),
]