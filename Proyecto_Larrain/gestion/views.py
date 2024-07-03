from django.shortcuts import render , redirect , get_object_or_404
from .models import Productos , Oferta
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import  UsuarioForm , OfertaForm , ClienteForm , ProductoForm
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib import messages

# Create your views here.
def index(request):
    user = request.user
    print(user)
    context = {'user':user}                                                           
    return render(request,'gestion/PaginaPrincipal.html',context)

def Pagina_Principal(request):
    tipo_producto = request.GET.get('tipo_producto')
    buscar_producto = request.GET.get('buscar_producto')

    productos = Productos.objects.all()

    if buscar_producto:
        productos = productos.filter(Q(nombre_producto__icontains=buscar_producto) | Q(tipo_producto__icontains=buscar_producto))
    

    if tipo_producto:
        productos = productos.filter(tipo_producto__icontains=tipo_producto)

    if not productos.exists():
        productos = []
    
    User = get_user_model()
    if request.user.is_authenticated and request.user.groups.filter(name='Agentes').exists():
        es_agente = True
    else:
        es_agente = False

    User = get_user_model()
    if request.user.is_authenticated and request.user.groups.filter(name='Supervisor_Local').exists():
        supervisor = True
    else:
        supervisor = False

    return render(request, 'gestion/Pagina_Principal.html', {'productos': productos, 'tipo_producto': tipo_producto, 'buscar_producto': buscar_producto,'es_agente': es_agente, 'supervisor':supervisor})

def quienes_somos(request):
    context={}
    Pagina_Principal
    return render(request, 'gestion/quienes_somos.html', context)

def donde_encontrarnos(request):
    context={}
    return render(request, 'gestion/donde_encontrarnos.html', context)

def login_sesion(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["contraseña"]
        user = authenticate(username=username,password=password)
        if user is not None:
            print("Usuario autenticado...")
            login(request, user)
            return redirect('PaginaPrincipal')
        else:
            return render(request,'gestion/login.html')
    else:
        return render(request,'gestion/login.html')
    
def logout_sesion(request):
    try:
        logout(request)
        return redirect('PaginaPrincipal')
    except:
        print("Error, no se pudo cerrar sesion...")
        return redirect('PaginaPrincipal')

@login_required
def perfil(request):
    try:
        user = User.objects.get(username=request.user)
        context = {}
        if user:
            print("Perfil...")
            if request.method == "POST":
                print("Edit, es un post...")
                form = UsuarioForm(request.POST,instance=request.user)
                form.save()
                return redirect('PaginaPrincipal')
            else:
                print("Edit, no es un post...")
                form = UsuarioForm(instance=request.user)
                mensaje = ""
                context = {"user":user,"form":form,"mensaje":mensaje}
                return render(request,'gestion/perfil.html',context)
    except:
        print("Error, perfil no existe...")
        return redirect('PaginaPrincipal')
def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PaginaPrincipal')  # Redirige a la página principal u otra página después del registro
    else:
        form = ClienteForm()
    return render(request, 'gestion/registro.html', {'form': form})

def ofertas(request):
    hoy = timezone.now().date()
    User = get_user_model()
    if request.user.is_authenticated and request.user.groups.filter(name='Agentes').exists():
        es_agente = True
    else:
        es_agente = False
    ofertas = Oferta.objects.filter(fecha_inicio__lte=hoy, fecha_fin__gte=hoy)
    print(f"Ofertas activas: {ofertas}")
    return render(request, 'gestion/ofertas.html', {'ofertas': ofertas, 'es_agente':es_agente})

    

def agregar_ofertas(request):
    if request.method =='POST':
        form = OfertaForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('ofertas')
    else:
        form= OfertaForm()
    return render(request,'gestion/agregar_ofertas.html', {'form':form})


def editar_productos(request, pk):
    producto = get_object_or_404(Productos, pk=pk)
    if request.method == 'POST':
        
        producto.nombre_producto = request.POST['nombre_producto']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.tipo_producto = request.POST['tipo_producto']
        if 'imagen' in request.FILES:
            producto.imagen = request.FILES['imagen']
        producto.save()
        return redirect('PaginaPrincipal') 
    context = {
        'producto': producto
    }
    return render(request, 'gestion/editar_productos.html', context)

def carrito_compras(request):
    context={}
    Pagina_Principal
    return render(request, 'gestion/carrito.html', context)

def eliminar_oferta(request, oferta_id):
    oferta = get_object_or_404(Oferta, id=oferta_id)
    
    if request.method == 'POST':
        oferta.delete()
        messages.success(request, 'La oferta ha sido eliminada exitosamente.')
        return redirect('ofertas') 
    
    return render(request, 'gestion/eliminar_oferta.html', {'oferta': oferta})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('PaginaPrincipal')
    else:
        form = ProductoForm()
    return render(request, 'gestion/agregar_productos.html', {'form': form})
