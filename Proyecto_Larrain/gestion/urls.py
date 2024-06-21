from django.urls import path

from . import views

urlpatterns=[
    path('PaginaPrincipal',views.Pagina_Principal,name='PaginaPrincipal'),
    path('QuienesSomos', views.quienes_somos, name='QuienesSomos'),
]