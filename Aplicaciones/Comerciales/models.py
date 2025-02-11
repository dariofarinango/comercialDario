from django.db import models

# Modelo para Edificaciones
class Edificacion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_estimada = models.DateTimeField()
    estado = models.CharField(max_length=50)
    presupuesto = models.CharField(max_length=100)
    foto = models.FileField(upload_to='edificaciones/')

    def __str__(self):
        return self.nombre
    

# Modelo para Tiendas
class Tienda(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    id_edificacion = models.ForeignKey(Edificacion, on_delete=models.CASCADE, related_name='tiendas')

    def __str__(self):
        return self.nombre

# Modelo para Propietarios
class Propietario(models.Model):
    nombre = models.CharField(max_length=255)
    foto = models.FileField(upload_to='propietarios/')
    direccion = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, related_name='propietarios')  # ✅ Relacionado con Tienda

    

    def __str__(self):
        return self.nombre

# Modelo para Fechas de Entrega
class FechaEntrega(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, related_name='fechas_entrega')  # ✅ Relacionado con Tienda
    fecha_entrega = models.DateTimeField()
    estado_entrega = models.CharField(max_length=50)

    def __str__(self):
        return f"Entrega para {self.id_edificacion.nombre} - {self.fecha_entrega}"

# Modelo para Recursos
class Recurso(models.Model):
    TIPO_RECURSO_CHOICES = [
        ('humano', 'Humano'),
        ('material', 'Material'),
        ('financiero', 'Financiero'),
    ]

    id_edificacion = models.ForeignKey(Edificacion, on_delete=models.CASCADE, related_name='recursos')
    tipo_recurso = models.CharField(max_length=50, choices=TIPO_RECURSO_CHOICES)
    descripcion = models.CharField(max_length=255)
    cantidad = models.CharField(max_length=50)
    costo = models.CharField(max_length=50)
    fecha_asignacion = models.DateTimeField()

    def __str__(self):
        return f"{self.tipo_recurso} - {self.descripcion}"
    



