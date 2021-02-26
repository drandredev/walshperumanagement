from django import forms
from biologia.models import *


class FormularioForm(forms.ModelForm):
    class Meta:
        model = BD_Integrada_Aves_Chinalco_Seca_2018
        fields='__all__'

class FormularioFotosIntegrado(forms.ModelForm):
    class Meta:
        model = Fotos_Integrado_Aves_Chinalco_Seca_2018
        fields='__all__'

class FormularioCoordenadasAves(forms.ModelForm):
    class Meta:
        model=CoordenadasIntegradasAves2018
        fields='__all__'

class FormularioHoja1(forms.ModelForm):
    class Meta:
        model= hoja1_BD
        fields='__all__'

class FormularioCoordenadas_BD(forms.ModelForm):
    class Meta:
        model= Coordenadas_BD
        fields='__all__'

class FormularioBitacora_Mamiferos(forms.ModelForm):
    class Meta:
        model= bitacora_BD_Mamiferos
        fields='__all__'

class FormularioHoja3_Vegetacion(forms.ModelForm):
    class Meta:
        model= Hoja3_BD_Vegetacion_2018
        fields='__all__'

class FormularioBdMamiferos(forms.ModelForm):
    class Meta:
        model= BD_mamiferos_BD_Mamiferos
        fields='__all__'

class FormularioBdAnfibiosReptiles(forms.ModelForm):
    class Meta:
        model= BD_anfibios_reptiles_BD
        fields='__all__'

class FormularioCoordenadasMamiferos(forms.ModelForm):
    class Meta:
        model= Coordenadas_reporte_BD_Mamiferos
        fields='__all__'

class FormularioEsfuerzoMamifero(forms.ModelForm):
    class Meta:
        model= Esfuerzo_Muestreo_BD_Mamiferos
        fields='__all__'

class Formulario_Vegetacion_CompensacionAmbiental(forms.ModelForm):
    class Meta:
        model= Compensacion_Ambiental_Vegetacion_2018
        fields='__all__'

class Formulario_Vegetacion_EsfuerzoMuestreo(forms.ModelForm):
    class Meta:
        model= Esfuerzo_Muestreo_BD_Vegetacion_2018
        fields='__all__'

class Formulario_Vegetacion_BD(forms.ModelForm):
    class Meta:
        model= Base_Datos_Vegetacion_2018
        fields='__all__'


class Formulario_BD_fotos_BD(forms.ModelForm):
    class Meta:
        model=BD_fotos_BD
        fields='__all__'
