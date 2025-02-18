from django.urls import path

from . import views

urlpatterns=[
    path('PaginaPrincipal',views.Pagina_Principal,name='PaginaPrincipal'),
    path('QuienesSomos', views.quienes_somos, name='QuienesSomos'),
    path('DondeEncontranos', views.donde_encontrarnos, name='DondeEncontranos'),
    path('login_sesion', views.login_sesion, name='login_sesion'),
    path('logout_sesion', views.logout_sesion, name='logout_sesion'),
    path('perfil',views.perfil,name='perfil'),
    path('registro', views.registrar_cliente, name='registro'),
    path('ofertas', views.ofertas,name='ofertas'),
    path('agregarOfertas', views.agregar_ofertas,name='agregarOfertas'),
    path('editar_productos/<str:pk>',views.editar_productos,name="editar_productos"),
    path('carrito', views.carrito, name='carrito'),
    path('eliminar_oferta/<int:oferta_id>/', views.eliminar_oferta, name='eliminar_oferta'),
    path('agregarProductos', views.agregar_producto, name='agregarProductos'),
    path('registroUsuario/', views.registrar_usuario, name='registroUsuario'),
    path('perfil_User',views.perfil_user,name='perfil_User'),
    path('detalle_producto/<str:pk>', views.detalle_producto, name='detalle_producto'),
    path('agregar_al_carrito/<str:pk>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_del_carrito/<str:pk>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]