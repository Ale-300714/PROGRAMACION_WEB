from django.contrib import admin
from .models import Cliente, Productos, Pedido, DetallePedido, Oferta, Agente, Proveedor, Compra, Despacho

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Productos)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Oferta)
admin.site.register(Agente)
admin.site.register(Proveedor)
admin.site.register(Compra)
admin.site.register(Despacho)
