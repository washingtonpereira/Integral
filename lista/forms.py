from django import forms
from .models import Lista

class FormularioCadastro (forms.ModelForm):
    class Meta:
        model = Lista
        fields = ('nome', 'preco')