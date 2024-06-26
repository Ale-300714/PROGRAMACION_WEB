from django.shortcuts import render , redirect
from .models import Productos
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import  UsuarioForm 
# Create your views here.

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

    return render(request, 'gestion/Pagina_Principal.html', {'productos': productos, 'tipo_producto': tipo_producto, 'buscar_producto': buscar_producto})

def quienes_somos(request):
    context={}
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
def registro_cliente(request):
    if request.method == 'POST':
        user_form = UsuarioForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('PaginaPrincipal')
    else:
        user_form = UsuarioForm()
    
    context = {
        'user_form': user_form,
    }
    return render(request, 'gestion/registro.html', context)