from django.shortcuts import render

# Create your views here.

def Pagina_Principal(request):
    context={}
    return render(request, 'gestion/Pagina_principal.html',context)