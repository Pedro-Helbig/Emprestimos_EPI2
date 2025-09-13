# equipamentos/forms.py
from django import forms
from colaboradores.models import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = [
            'categoria', 'nome', 'descricao', 'marca', 'modelo',
            'numero_serie', 'numero_ca', 'data_fabricacao', 'data_validade',
            'tamanho', 'cor', 'valor_unitario', 'status', 'ativo'
        ]