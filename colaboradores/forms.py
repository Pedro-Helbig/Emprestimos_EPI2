from django import forms
from .models import Colaborador

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = "__all__"
        widgets = {
            'data_admissao': forms.DateInput(attrs={'type': 'date'}),
        }