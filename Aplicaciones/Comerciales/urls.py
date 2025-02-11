from django.urls import path
from . import views 

urlpatterns = [
   # ---------------------------------------------------inicio.html---------------------------------------------------
    path('', views.inicio, name='inicio'),

   #-------------------------------------------------edificaciones.html-----------------------------------------------
    path('edificaciones/', views.listar_edificaciones, name='listar_edificaciones'),
    path('edificaciones/nueva/', views.nueva_edificacion, name='nueva_edificacion'),
    path('edificaciones/editar/<int:id>/', views.editar_edificacion, name='editar_edificacion'),
    path('edificaciones/eliminar/<int:id>/', views.eliminar_edificacion, name='eliminar_edificacion'),

   #------------------------------------------------------Tiendas.html-------------------------------------------------------
    path('tiendas/', views.listar_tiendas, name='listar_tiendas'),
    path('tiendas/nueva/', views.nueva_tienda, name='nueva_tienda'),
    path('tiendas/editar/<int:id>/', views.editar_tienda, name='editar_tienda'),
    path('tiendas/eliminar/<int:id>/', views.eliminar_tienda, name='eliminar_tienda'),

   #------------------------------------------------------Propietario.html------------------------------------------------
    path('propietarios/', views.listar_propietarios, name='listar_propietarios'),
    path('propietarios/nuevo/', views.nuevo_propietario, name='nuevo_propietario'),
    path('propietarios/editar/<int:id>/', views.editar_propietario, name='editar_propietario'),
    path('propietarios/eliminar/<int:id>/', views.eliminar_propietario, name='eliminar_propietario'),

    #--------------------------------------------------------FechaEntrega------------------------------------------------
    path('entregas/', views.listar_entregas, name='listar_entregas'),
    path('entregas/nueva/', views.nueva_entrega, name='nueva_entrega'),
    path('entregas/editar/<int:id>/', views.editar_entrega, name='editar_entrega'),
    path('entregas/eliminar/<int:id>/', views.eliminar_entrega, name='eliminar_entrega'),

    #---------------------------------------------------------Recursoso.html-------------------------------------
    path('recursos/', views.listar_recursos, name='listar_recursos'),
    path('recursos/nuevo/', views.nuevo_recurso, name='nuevo_recurso'),
    path('recursos/editar/<int:id>/', views.editar_recurso, name='editar_recurso'),
    path('recursos/eliminar/<int:id>/', views.eliminar_recurso, name='eliminar_recurso'),

    #*-------------------------------------------- URL para acceder al reporte-----------------------------------
    path('reporte/', views.reportes, name='reportes'),


   
    
]