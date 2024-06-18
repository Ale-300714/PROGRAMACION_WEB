from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    contraseña= models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return str(self.nombre)+ "" + str(self.apellido_paterno)


class Productos(models.Model):
    nombre_producto = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock= models.IntegerField()
    tipo_producto = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre_producto

class Pedido(models.Model):
    Estado =[
        ('pendiente', 'Pendiente'),
        ('procesando', 'Procesando'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
    ]

    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    fecha_pedido=models.DateField(auto_now_add=True)
    estado_pedido = models.CharField(max_length=50, choices=Estado, default='pendiente')
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nombre}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad= models.IntegerField()
    subtotal= models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.cantidad } x {self.producto.nombre_producto}"


class Oferta(models.Model):
    producto= models.ForeignKey(Productos, on_delete=models.CASCADE)
    precio_oferta= models.DecimalField(max_digits=10,decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin= models.DateField()

    def __str__(self):
        return f"Oferta {self.id} - {self.producto.nombre_producto}"
    
class Agente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    email= models.EmailField(unique=True)
    telefono= models.CharField(max_length=20)
    localizacion = models.CharField(max_length=255)

    def __str__(self):
        return str(self.nombre) + "" + str(self.apellido_paterno)
class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return str(self.nombre_proveedor)

class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_compra = models.DateField()
    fecha_recepcion = models.DateField()

    def __str__(self):
        return f"Compra {self.id} - {self.producto.nombre_producto}"

class Despacho(models.Model):
    Estado_Despacho = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('despachado','Despachado'),
        ('entregado','Entregado'),
    ]
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    fecha_despacho = models.DateField()
    direccion_entrega= models.CharField(max_length=300)
    estado_despacho= models.CharField(max_length=50, choices=Estado_Despacho,default='pendiente')

    def __str__(self) :
        return f"Despachoi {self.id} - {self.pedido.id}"



