from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection 
from .forms import ContactoForm
from .models import Product, Contacto, Carrito

def agradecimiento(request):
    return render(request, 'Gracias_compra.html')

def index(request):
    productos = Product.objects.all()
    return render(request, 'product_list.html', {'productos': productos})

def raw_product_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT name, description, price, stock, created_at, image FROM mydino_Product")
        productos = cursor.fetchall()
    return render(request, 'raw_product_list.html', {'productos': productos})
@login_required
def producto_detalle(request, pk):
    producto2 = get_object_or_404(Product, pk=pk)
    return render(request, 'producto_detalle.html', {'producto2': producto2})
@login_required
def agregar_al_carrito(request, product_id):
    producto = get_object_or_404(Product, id=product_id)
    carrito_item, created = Carrito.objects.get_or_create(producto=producto)
    
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()

    return redirect('ver_carrito')
@login_required
def eliminar_del_carrito(request, product_id):
    producto = get_object_or_404(Product, id=product_id)
    carrito_item = Carrito.objects.get(producto=producto)
    
    if carrito_item.cantidad > 1:
        carrito_item.cantidad -= 1
        carrito_item.save()
    else:
        carrito_item.delete()

    return redirect('ver_carrito')
@login_required
def limpiar_carrito(request):
    Carrito.objects.all().delete()
    return redirect('ver_carrito')
@login_required
def comprar(request):
    Carrito.objects.all().delete()
    return redirect('agradecimiento')
@login_required
def ver_carrito(request):
    carrito_items = Carrito.objects.all()
    total = sum(item.producto.price * item.cantidad for item in carrito_items)
    return render(request, 'carrito.html', {'carrito_items': carrito_items, 'total': total})



@login_required
def contacto_nuevo(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_confirmacion')
    else:
        form = ContactoForm()
    return render(request, 'mydino/contacto_formulario.html', {'form': form})

# Vista para ver el detalle de un contacto específico
@login_required
def contacto_detalle(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    return render(request, 'mydino/contacto_detalle.html', {'contacto': contacto})



def contacto_lista(request):
    contactos = Contacto.objects.all()
    return render(request, 'mydino/contacto_lista.html', {'contactos': contactos})

def contacto_confirmacion(request):
    return render(request, 'mydino/contacto_confirmacion.html')

@login_required
def vista_protegida(request):
    return render(request, 'vista_protegida.html')
