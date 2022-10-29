from django.shortcuts import render, redirect

from reservas_APP.forms import FormReserva
from reservas_APP.models import Reservas

# Create your views here.

def index(request):
    return render(request, 'index.html')

def agendar_reserva(request):
    form = FormReserva()
    if request.method == 'POST':
        form = FormReserva(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listado_reservas)
        
    data = {'form': form}
    return render(request, 'agendar_reserva.html', data)

def listado_reservas(request):
    reservas = Reservas.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reservas.html', data)

def eliminar_reserva(request, id):
    reserva = Reservas.objects.get(id = id)
    reserva.delete()
    return redirect('listado_reservas')

def actualizar_reserva(request, id):
    reserva = Reservas.objects.get(id = id)
    form = FormReserva(instance=reserva)
    if request.method == 'POST':
        form = FormReserva(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect(listado_reservas)
    data = {'form' : form}
    return render(request, 'agendar_reserva.html', data)