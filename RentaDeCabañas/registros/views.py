from django.shortcuts import render
from .models import Cabañas
from .models import Promociones
from .models import Reservacion
from .forms import ReservacionForm
# Create your views here.
def registros(request):
    cabañas=Cabañas.objects.all() #Recuperar los objetos de la bd 
    return render(request, "registros/principal.html",{'cabañas':cabañas}) #inidicamos el lugar donde se renderizara el resultado de esta vsita y enviamos la lista de alumnos

def clasificados(request):
    promociones=Promociones.objects.all() #Recuperar los objetos de la bd 
    return render(request, "registros/clasificados.html",{'promociones':promociones}) #inidicamos el lugar donde se renderizara el resultado de esta vsita y enviamos la lista de alumnos

def registrar(request):
    if request.method == 'POST':
        form = ReservacionForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save()#inserta 
            reservacion=Reservacion.objects.all()
            return render(request,"registros/consultaReservacion.html",{'reservacion':reservacion})
    form = ReservacionForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request, 'registros/Reservaciones.html', {'form':form})

def reservar(request):
    return render(request,"registros/Reservaciones.html")

#def consultar(request):
   # reservacion=Reservacion.objects.all()
    #all recupera todos los objetos del modelo (registros en la tabla)
    #return render(request,"registros/consultaReservacion.html",{'reservacion':reservacion})
