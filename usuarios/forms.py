from django import forms
from .models import CustomUser, Cliente, Funcionario
from inventory.models import Loja

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class FuncionarioForm(forms.ModelForm):

    loja = forms.ModelChoiceField(queryset=Loja.objects.all())

    class Meta:
        model = Funcionario
        fields = ['username', 'email', 'password', 'first_name', 'last_name','loja']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
