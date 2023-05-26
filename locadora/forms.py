from django import forms
from locadora.models import Aluguel

class AluguelForm(forms.ModelForm):
    class Meta:
        model = Aluguel
        exclude = ('hash_aleatoria',)
        widgets = {
            'data_retirada': forms.DateTimeInput(attrs={'class': 'datetime-input', 'placeholder': 'YYYY-MM-DD HH:MM'}),
            'data_entrega': forms.DateTimeInput(attrs={'class': 'datetime-input', 'placeholder': 'YYYY-MM-DD HH:MM'}),
        }