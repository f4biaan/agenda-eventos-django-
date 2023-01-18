from django.shortcuts import render, redirect
from .forms import EventoForm
from .models import Eventos

# Create your views here.
def list_eventos(request):
    eventos = Eventos.objects.values()
    context = {'eventos': eventos}
    return render(request, 'eventos/list-eventos.html', context)


def create_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = EventoForm()
    return render(request, 'eventos/crear-evento.html', {'form': form})

def update_eventos(request, id):
    evento = Eventos.objects.get(id=id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/update-evento.html', {'form': form, 'id': id})

def delete_eventos(request, id):
    person = Eventos.objects.get(id=id)
    person.delete()
    return redirect('')