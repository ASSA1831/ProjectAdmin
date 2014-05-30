from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pmi/' , include('pmi.urls', namespace="pmi")),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}),
    #url(r'^Editar_proyecto/informacion_tareas/agregar_tarea/$', crearTarea),
    #url(r'^proyectos/$', proyectos),
    #url(r'^Editar_proyecto/informacion_proyecto/$', informacionDeProyecto),
    #url(r'^crear_proyecto/$', crearProyecto),
    #url(r'^Editar_proyecto/informacion_tareas/$', informeTareas),
    #url(r'^Editar_proyecto/$', editarProyecto),
)
