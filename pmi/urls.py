
from django.conf.urls import patterns, url

from pmi import views

urlpatterns = patterns('',
    url(r'^editar_proyecto/informacion_proyecto/editar_informacion_proyecto/$', views.editarInformacionProyecto, name="editarInformacionProyecto"),
    url(r'^editar_proyecto/informacion_tareas/agregar_tarea/$', views.crearTarea, name="crearTarea"),
    url(r'^proyectos/$', views.proyectos, name="proyectos"),
    url(r'^editar_proyecto/informacion_proyecto/$', views.informacionDeProyecto, name="informacionDeProyecto"),
    url(r'^crear_proyecto/$', views.crearProyecto, name="crearProyecto"),
    url(r'^editar_proyecto/informacion_tareas/$', views.informeTareas, name="informeTareas"),
    url(r'^editar_proyecto/$', views.editarProyecto, name="editarProyecto"),
    url(r'^guardar_proyecto/$', views.guardarProyecto, name="guardarProyecto"),
    url(r'^guardar_tarea/$', views.guardarTarea, name="guardarTarea"),
    url(r'^informe_tareas/$', views.printInformeTareas, name="printInformeTareas"),
    
   
    
    


    
)
