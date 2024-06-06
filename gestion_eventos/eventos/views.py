from django.shortcuts import render, redirect
from .forms import FormEvent
from .models import Event
from django.contrib import messages

def view_event(request):
    form = FormEvent(request.POST or None)
    events = Event.objects.all()

    if request.method == 'POST' and form.is_valid():
        try:
            form.save()
            messages.success(request, 'Evento registrado con éxito.')
            return redirect('eventos')
        except Exception as e:
            messages.error(request, f'Ocurrió un error al registrar el evento: {e}')
        return redirect('eventos')
    
    return render(request, "eventos/evento_list.html", {'form': form, 'eventos': events})

