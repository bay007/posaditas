from django.contrib import admin
from django import forms
from posadas.models import Posada

class PosadaAdminForm(forms.ModelForm):
    class Meta:
        model = Posada
        fields = '__all__'


class PosadaAdmin(admin.ModelAdmin):
    form = PosadaAdminForm
    list_display = ['ubicacion', 'nombre', 'fecha', 'horario']

admin.site.register(Posada, PosadaAdmin)