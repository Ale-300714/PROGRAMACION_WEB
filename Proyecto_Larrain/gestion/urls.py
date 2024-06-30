from django.urls import path

from . import views

urlpatterns=[
    path('PaginaPrincipal',views.Pagina_Principal,name='PaginaPrincipal'),
    path('QuienesSomos', views.quienes_somos, name='QuienesSomos'),
    path('DondeEncontranos', views.donde_encontrarnos, name='DondeEncontranos'),
    path('login_sesion', views.login_sesion, name='login_sesion'),
    path('logout_sesion', views.logout_sesion, name='logout_sesion'),
    path('perfil',views.perfil,name='perfil'),
    path('registro', views.registro_cliente, name='registro'),
    path('ofertas', views.ofertas,name='ofertas'),
    path('agregarOfertas', views.agregar_ofertas,name='agregarOfertas'),
]