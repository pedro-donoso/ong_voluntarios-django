from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages

from .models import Voluntario, Evento

from .forms import VoluntarioForm, EventoForm

# Vistas Voluntarios

def voluntario_list(request):
    voluntarios = Voluntario.objects.all().order_by('nombre')
    return render(request, 'gestion/voluntario_list.html', {'voluntarios': voluntarios})

def voluntario_create(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Voluntario creado exitosamente')
            return redirect('voluntario_list')
    else:
        form = VoluntarioForm()
    return render(request, 'gestion/voluntario_form.html', {'form': form, 'titulo': 'Nuevo Voluntario'})

def voluntario_edit(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    if request.method == 'POST':
        form = VoluntarioForm(request.POST, instance=voluntario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Voluntario actualizado')
            return redirect('voluntario_list')
    else:
        form = VoluntarioForm(instance=voluntario)
    return render(request, 'gestion/voluntario_form.html', {'form': form, 'titulo': f'Editar {voluntario.nombre}'})

def voluntario_delete(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    if request.method == 'POST':
        voluntario.delete()
        messages.success(request, 'Voluntario eliminado')
        return redirect('voluntario_list')
    return render(request, 'gestion/voluntario_confirm_delete.html', {'voluntario': voluntario})

# Vistas Eventos

def evento_list(request):
    eventos = Evento.objects.all()
    return render(request, 'gestion/evento_list.html', {'eventos': eventos})

def evento_create(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento creado exitosamente')
            return redirect('evento_list')
    else:
        form = EventoForm()
    return render(request, 'gestion/evento_form.html', {'form': form, 'titulo': 'Nuevo Evento'})

def evento_edit(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento actualizado')
            return redirect('evento_list')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'gestion/evento_form.html', {'form': form, 'titulo': f'Editar {evento.titulo}'})

def evento_delete(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        messages.success(request, 'Evento eliminado')
        return redirect('evento_list')
    return render(request, 'gestion/evento_confirm_delete.html', {'evento': evento})
