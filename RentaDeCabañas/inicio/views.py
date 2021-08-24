from django.shortcuts import render, HttpResponse


# Create your views here.
def principal(request):

    return render(request, "inicio/principal.html")

def clasificados (request):

    return render(request, "inicio/clasificados.html")


def login(request):

    return render(request, "inicio/login.html")
    

def contacto(request):

    return render(request, "inicio/contacto.html")

def QuieneSomos(request):

    return render(request, "inicio/Quienes_Somos.html")
