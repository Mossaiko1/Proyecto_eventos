from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm
from django.contrib import messages

def event_list(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EventForm()
    
    events = Event.objects.all()
    return render(request, 'eventos/event_list.html', {'form': form, 'events': events})

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'eventos/edit_event.html', {'form': form})


def confirm_delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'El evento ha sido eliminado con éxito.')
        return redirect('event_list')
    
    return render(request, 'eventos/confirm_delete.html', {'event': event})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    messages.success(request, 'El evento ha sido eliminado con éxito.')
    return redirect('event_list')