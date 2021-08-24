from django import forms
from .models import Reservacion

class ReservacionForm(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ['cliente','numHu','fllegada','fsalida']