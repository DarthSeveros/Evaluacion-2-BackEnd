from django import forms
from reservas_APP.models import Reservas
from django.core.exceptions import ValidationError

class FormReserva(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = '__all__'
        widgets = {
            'nombre_persona': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'telefono': forms.TextInput(attrs={'placeholder': '12345678'}),
            'fecha_reserva': forms.TextInput(attrs={'placeholder': 'aaaa-mm-dd'}),
            'hora_reserva': forms.TextInput(attrs={'placeholder': 'hh:mm'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        cantidad_personas = cleaned_data.get('cantidad_personas')
        telefono = cleaned_data.get('telefono')
        if len(telefono) < 8:
            self.add_error('telefono', 'El número de teléfono es demasiado corto')
        if cantidad_personas < 1:
            self.add_error('cantidad_personas', 'EL número de personas es menor a 1') 
        if cantidad_personas > 15:
            self.add_error('cantidad_personas', 'El número de personas es mayor a 15')
        return self.cleaned_data
