from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Edificacion, Tienda, Propietario, FechaEntrega, Recurso
# Create your views here.
from django.db.models import Q
from django.contrib import messages
# ---------------------------------------------------inicio.html---------------------------------------------------
def inicio(request):
    return render(request, 'inicio.html')

#----------------------------------------------------Edificaciones.html----------------------------------------
def listar_edificaciones(request):
    edificaciones = Edificacion.objects.all()
    return render(request, 'edificaciones/listoEdificaciones.html', {'edificaciones': edificaciones})

def nueva_edificacion(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        fecha_inicio = request.POST["fecha_inicio"]
        fecha_estimada = request.POST["fecha_estimada"]
        estado = request.POST["estado"] 
        presupuesto = request.POST["presupuesto"]
        foto = request.FILES.get("foto")
        
        Edificacion.objects.create(
            nombre=nombre, descripcion=descripcion, fecha_inicio=fecha_inicio,
            fecha_estimada=fecha_estimada, estado=estado, presupuesto=presupuesto, foto=foto
        )
        messages.success(request, " ***********Guardado Exitosamente************")
        return redirect('listar_edificaciones')
    
    return render(request, 'edificaciones/nuevoEdificacion.html')

def editar_edificacion(request, id):
    edificacion = get_object_or_404(Edificacion, id=id)
    if request.method == "POST":
        edificacion.nombre = request.POST["nombre"]
        edificacion.descripcion = request.POST["descripcion"]
        edificacion.fecha_inicio = request.POST["fecha_inicio"]
        edificacion.fecha_estimada = request.POST["fecha_estimada"]
        edificacion.estado = request.POST["estado"]
        edificacion.presupuesto = request.POST["presupuesto"]
        if "foto" in request.FILES:
            edificacion.foto = request.FILES["foto"]
        edificacion.save()
        messages.success(request, " ***********Editado Exitosamente************")
        return redirect('listar_edificaciones')
        
    return render(request, 'edificaciones/editarEdificaciones.html', {'edificacion': edificacion})

def eliminar_edificacion(request, id):
    edificacion = get_object_or_404(Edificacion, id=id)
    edificacion.delete()
    return redirect('listar_edificaciones')

#--------------------------------------------------------Tiendas.html-------------------------------------------------------
def listar_tiendas(request):
    tiendas = Tienda.objects.all()
    return render(request, 'tiendas/listadoTienda.html', {'tiendas': tiendas})

def nueva_tienda(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        direccion = request.POST["direccion"]
        id_edificacion = request.POST["id_edificacion"]
        edificacion = get_object_or_404(Edificacion, id=id_edificacion)
        
        Tienda.objects.create(
            nombre=nombre, 
            direccion=direccion, 
            id_edificacion=edificacion
        )
        messages.success(request, " ***********Guardado Exitosamente************")
        return redirect('listar_tiendas')
    
    edificaciones = Edificacion.objects.all()
    return render(request, 'tiendas/nuevoTienda.html', {'edificaciones': edificaciones})

def editar_tienda(request, id):
    tienda = get_object_or_404(Tienda, id=id)
    if request.method == "POST":
        tienda.nombre = request.POST["nombre"]
        tienda.direccion = request.POST["direccion"]
        tienda.id_edificacion = get_object_or_404(Edificacion, id=request.POST["id_edificacion"])
        tienda.save()
        messages.success(request, " ***********Editado Exitosamente************")
        return redirect('listar_tiendas')
    
    edificaciones = Edificacion.objects.all()
    return render(request, 'tiendas/editarTienda.html', {'tienda': tienda, 'edificaciones': edificaciones})

def eliminar_tienda(request, id):
    tienda = get_object_or_404(Tienda, id=id)
    tienda.delete()
    return redirect('listar_tiendas')

#--------------------------------------------------------Propietario.html------------------------------------------------
def listar_propietarios(request):
    propietarios = Propietario.objects.all()
    return render(request, 'propietario/listadoPropietario.html', {'propietarios': propietarios})

def nuevo_propietario(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        foto = request.FILES.get("foto")
        direccion = request.POST["direccion"]
        contacto = request.POST["contacto"]
        tienda_id = request.POST["tienda"]
        tienda = get_object_or_404(Tienda, id=tienda_id)
        
        Propietario.objects.create(
            nombre=nombre,
            foto=foto,
            direccion=direccion,
            contacto=contacto,
            tienda=tienda
        )
        messages.success(request, " ***********Guardado Exitosamente************")
        return redirect('listar_propietarios')
    
    tiendas = Tienda.objects.all()
    return render(request, 'propietario/nuevoPropietario.html', {'tiendas': tiendas})

def editar_propietario(request, id):
    propietario = get_object_or_404(Propietario, id=id)
    if request.method == "POST":
        propietario.nombre = request.POST["nombre"]
        if "foto" in request.FILES:
            propietario.foto = request.FILES["foto"]
        propietario.direccion = request.POST["direccion"]
        propietario.contacto = request.POST["contacto"]
        propietario.tienda = get_object_or_404(Tienda, id=request.POST["tienda"])
        propietario.save()

        messages.success(request, " ***********Editado Exitosamente************")
        return redirect('listar_propietarios')
    
    tiendas = Tienda.objects.all()
    return render(request, 'propietario/editarPropietario.html', {'propietario': propietario, 'tiendas': tiendas})

def eliminar_propietario(request, id):
    propietario = get_object_or_404(Propietario, id=id)
    propietario.delete()
    return redirect('listar_propietarios')

#---------------------------------------------------------FechaEntrega.html----------------------------------------------------

# Listado de Fechas de Entrega
def listar_entregas(request):
    entregas = FechaEntrega.objects.all()
    return render(request, 'fecha/ListadoEntrega.html', {'entregas': entregas})

# Crear nueva Fecha de Entrega
def nueva_entrega(request):
    if request.method == "POST":
        tienda_id = request.POST.get('tienda')
        fecha_entrega = request.POST.get('fecha_entrega')
        estado_entrega = request.POST.get('estado_entrega')

        tienda = get_object_or_404(Tienda, id=tienda_id)

        FechaEntrega.objects.create(
            tienda=tienda,
            fecha_entrega=fecha_entrega,
            estado_entrega=estado_entrega
        )

        messages.success(request, " ***********Guardado Exitosamente************")
        return redirect('listar_entregas')

    tiendas = Tienda.objects.all()
    return render(request, 'fecha/nuevoEntrega.html', {'tiendas': tiendas})

# Editar Fecha de Entrega
def editar_entrega(request, id):
    entrega = get_object_or_404(FechaEntrega, id=id)
    tiendas = Tienda.objects.all()  # Obtener todas las tiendas

    if request.method == "POST":
        entrega.tienda = get_object_or_404(Tienda, id=request.POST.get('tienda'))
        entrega.fecha_entrega = request.POST.get('fecha_entrega')
        entrega.estado_entrega = request.POST.get('estado_entrega')
        entrega.save()

        messages.success(request, " ***********Editado Exitosamente************")
        return redirect('listar_entregas')

    return render(request, 'fecha/editarEntrega.html', {'entrega': entrega, 'tiendas': tiendas})

# Eliminar Fecha de Entrega
def eliminar_entrega(request, id):
    entrega = get_object_or_404(FechaEntrega, id=id)
    entrega.delete()
    return redirect('listar_entregas')

#-------------------------------------------------------------Recursos.html-----------------------------------------

# Listar Recursos
def listar_recursos(request):
    recursos = Recurso.objects.all()
    return render(request, 'recursos/listadoRecurso.html', {'recursos': recursos})

# Crear Recurso
def nuevo_recurso(request):
    if request.method == "POST":
        id_edificacion = request.POST.get('id_edificacion')
        tipo_recurso = request.POST.get('tipo_recurso')
        descripcion = request.POST.get('descripcion')
        cantidad = request.POST.get('cantidad')
        costo = request.POST.get('costo')
        fecha_asignacion = request.POST.get('fecha_asignacion')

        edificacion = get_object_or_404(Edificacion, id=id_edificacion)

        Recurso.objects.create(
            id_edificacion=edificacion,
            tipo_recurso=tipo_recurso,
            descripcion=descripcion,
            cantidad=cantidad,
            costo=costo,
            fecha_asignacion=fecha_asignacion
        )

        messages.success(request, " ***********Guardado Exitosamente************")
        return redirect('listar_recursos')

    edificaciones = Edificacion.objects.all()
    return render(request, 'recursos/nuevoRecurso.html', {'edificaciones': edificaciones})

# Editar Recurso
def editar_recurso(request, id):
    recurso = get_object_or_404(Recurso, id=id)

    if request.method == "POST":
        recurso.tipo_recurso = request.POST.get('tipo_recurso')
        recurso.descripcion = request.POST.get('descripcion')
        recurso.cantidad = request.POST.get('cantidad')
        recurso.costo = request.POST.get('costo')
        recurso.fecha_asignacion = request.POST.get('fecha_asignacion')
        recurso.save()

        messages.success(request, " ***********Editado Exitosamente************")
        return redirect('listar_recursos')

    return render(request, 'recursos/editarRecurso.html', {'recurso': recurso})

# Eliminar Recurso
def eliminar_recurso(request, id):
    recurso = get_object_or_404(Recurso, id=id)
    recurso.delete()
    return redirect('listar_recursos')

#---------------------------------------------------Reporte.html---------------------------------------


def reportes(request):
    # Obtener todos los objetos para los filtros
    edificaciones = Edificacion.objects.all()
    tiendas = Tienda.objects.all()
    propietarios = Propietario.objects.all()

    # Inicializar las variables de filtro
    filtro_edificacion = request.GET.get('edificacion')
    filtro_tienda = request.GET.get('tienda')
    filtro_propietario = request.GET.get('propietario')
    filtro_fecha_inicio = request.GET.get('fecha_inicio')
    filtro_fecha_fin = request.GET.get('fecha_fin')

    # Filtrar Fechas de Entrega
    fechas_entrega = FechaEntrega.objects.all()
    if filtro_edificacion:
        fechas_entrega = fechas_entrega.filter(tienda__id_edificacion__id=filtro_edificacion)
    if filtro_tienda:
        fechas_entrega = fechas_entrega.filter(tienda__id=filtro_tienda)
    if filtro_fecha_inicio and filtro_fecha_fin:
        fechas_entrega = fechas_entrega.filter(fecha_entrega__range=[filtro_fecha_inicio, filtro_fecha_fin])

    # Filtrar Recursos
    recursos = Recurso.objects.all()
    if filtro_edificacion:
        recursos = recursos.filter(id_edificacion__id=filtro_edificacion)
    if filtro_fecha_inicio and filtro_fecha_fin:
        recursos = recursos.filter(fecha_asignacion__range=[filtro_fecha_inicio, filtro_fecha_fin])

    # Filtrar Propietarios
    if filtro_propietario:
        propietarios_filtrados = Propietario.objects.filter(id=filtro_propietario)
    else:
        propietarios_filtrados = Propietario.objects.all()

    context = {
        'edificaciones': edificaciones,
        'tiendas': tiendas,
        'propietarios': propietarios,
        'fechas_entrega': fechas_entrega,
        'recursos': recursos,
        'propietarios_filtrados': propietarios_filtrados,
    }

    return render(request, 'reporte.html', context)