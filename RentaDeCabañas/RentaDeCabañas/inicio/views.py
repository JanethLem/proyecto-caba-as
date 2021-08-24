from django.shortcuts import render, HttpResponse

menu="""

"""
# Create your views here.
def principal(request):

    return render(request, "inicio/principal.html")


def clasificados(request):

    return render(request, "inicio/clasificados.html")


def cotizacion(request):

    return render(request, "inicio/cotizacion.html")


def login(request):

    return render(request, "inicio/login.html")
    

def contacto(request):

    return render(request, "inicio/contacto.html")

def ejemplo(request):

    return render(request, "inicio/ejemplo.html")










