from django import forms
from locadora.models import Aluguel

class AluguelForm(forms.ModelForm):
    class Meta:
        model = Aluguel
        exclude = ('hash_aleatoria',)
        widgets = {
            'data_retirada': forms.DateInput(attrs={'class': 'date-input', 'placeholder': 'YYYY-MM-DD'}),
            'data_entrega': forms.DateInput(attrs={'class': 'date-input', 'placeholder': 'YYYY-MM-DD'}),
        }