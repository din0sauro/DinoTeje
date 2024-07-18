from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.index, name='index'),
    path('contacto/nuevo/', views.contacto_nuevo, name='contacto_nuevo'),
    path('contacto/<int:pk>/', views.contacto_detalle, name='contacto_detalle'),
    path('contactos/', views.contacto_lista, name='contacto_lista'),
    path('contacto/confirmacion/', views.contacto_confirmacion, name='contacto_confirmacion'),
    path('vista_protegida/', views.vista_protegida, name='vista_protegida'),
    path('producto/<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('raw/', views.raw_product_list, name='raw_product_list'),
    path('raw/', views.raw_product_list, name='raw_product_list'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:product_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:product_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/limpiar/', views.limpiar_carrito, name='limpiar_carrito'),
    path('comprar/', views.comprar, name='comprar'),
    path('agradecimiento/', views.agradecimiento, name='agradecimiento'),
]
