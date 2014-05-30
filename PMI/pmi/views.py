from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse,  HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

import datetime
from pmi.models import *
import time



def crearTarea(request):
    proyecto_lista= Proyecto.objects.all()
    return render(request, 'agregarTarea.html', {'proyecto_lista': proyecto_lista})

def guardarTarea(request):
    proyecto = get_object_or_404(Proyecto, pk=request.POST['proyecto'])
    proyecto.tarea_set.create(nombre=request.POST["nombre"], comienzo=request.POST["comienzo"], final=request.POST["final"])
    return HttpResponseRedirect(reverse('pmi:informeTareas'))


def proyectos(request):
    proyecto_lista = Proyecto.objects.all()
    return render(request, 'proyectos.html', {'proyecto_lista': proyecto_lista})

def informacionDeProyecto(request):
    proyecto_lista = Proyecto.objects.all()
    
    return render(request, 'Informacion_de_proyecto.html', {'proyecto_lista': proyecto_lista})
    
def editarInformacionProyecto(request):
    proyecto_lista = Proyecto.objects.all()
    if request.POST.get("ver"):	
    	proyecto = get_object_or_404(Proyecto, pk=request.POST['proyecto'])   
    	nombre=proyecto.nombre
    	descripcion= proyecto.descripcion
        comienzo = proyecto.comienzo_pro 
    	final = proyecto.final_pro
	return render(request,'Informacion_de_proyecto.html', {'proyecto_lista': proyecto_lista, "proyecto": proyecto } )
    if request.POST.get("eliminar"):
	proyecto_lista = Proyecto.objects.all()
	proyecto = get_object_or_404(Proyecto, pk=request.POST['proyecto'])
        proyecto.delete()
        return HttpResponseRedirect(reverse('pmi:proyectos'))
    if request.POST.get("guardar"):
	proyecto = get_object_or_404(Proyecto, pk=request.POST['proyecto'])
	proyecto.descripcion= request.POST.get("descripcion2")
	proyecto.comienzo_pro= request.POST.get("nueva_fecha1")
	proyecto.final_pro= request.POST.get("nueva_fecha2")
	
	proyecto.save()
	return HttpResponseRedirect(reverse('pmi:proyectos'))
	
    return render(request,'Informacion_de_proyecto.html', {'proyecto_lista': proyecto_lista } )

@permission_required('pmi.crearProyecto')

def crearProyecto(request):
    return render(request, 'crear_proyecto.html')

def guardarProyecto(request):
    proyecto = Proyecto(nombre=request.POST["nombre"],comienzo_pro=request.POST["comienzo_pro"], final_pro=request.POST["final_pro"], descripcion=request.POST["descripcion"])  
    proyecto.save()
    return HttpResponseRedirect(reverse('pmi:proyectos'))



def informeTareas(request):
    proyecto_lista = Proyecto.objects.all()
    tareas_lista = Tarea.objects.all() 
    
	
    return render(request, 'informacionDeTareas.html',  {'proyecto_lista': proyecto_lista,"tareas_lista": tareas_lista })
  
def eliminarTarea(request):
    proyecto = get_object_or_404(Proyecto, pk=request.POST['proyecto']) 
    proyecto_lista = Proyecto.objects.all()
    tareas_lista = Tarea.objects.filter(proyecto=proyecto)
    return render(request,'informacionDeTareas.html', {'proyecto_lista': proyecto_lista, "tareas_lista": tareas_lista } )
    
def printInformeTareas(request):
    proyecto = get_object_or_404(Proyecto, pk=request.POST['proyecto']) 
    proyecto_lista = Proyecto.objects.all()
    tareas_lista = Tarea.objects.all()
    if request.POST.get("agregar"):
	return HttpResponseRedirect(reverse('pmi:crearTarea'))
    if request.POST.get("filtrar"):
        proyecto_lista = Proyecto.objects.all()
	tareas_lista = Tarea.objects.filter(proyecto=proyecto)
        return render(request,'informacionDeTareas.html', {'proyecto_lista': proyecto_lista, "tareas_lista": tareas_lista } )
    if request.POST.get("eliminar"):
	proyecto_lista = Proyecto.objects.all()
        tareas_lista = Tarea.objects.all()
	tareaid=request.POST.get("select_tarea")
        tarea= get_object_or_404(Tarea, pk= tareaid)
        tarea.delete()
	return render(request,'informacionDeTareas.html', {'proyecto_lista': proyecto_lista, "tareas_lista": tareas_lista } )
      
    return render(request,'informacionDeTareas.html', {'proyecto_lista': proyecto_lista, "tareas_lista": tareas_lista } )
@permission_required('pmi.editarProyecto')
def editarProyecto(request):
    return HttpResponseRedirect(reverse('pmi:informacionDeProyecto'))
