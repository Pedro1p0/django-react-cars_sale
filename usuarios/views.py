from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import CustomUser, Cliente, Funcionario, FuncionarioProfile, ClienteProfile
from .forms import CustomUserForm, ClienteForm, FuncionarioForm
from inventory.models import Loja
from .decorators import login_and_role_required
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password


class CustomUserCreateView(View):
    def get(self, request):
        form = CustomUserForm()
        return render(request, 'customuser_form.html', {'form': form})

    def post(self, request):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('customuser-list'))
        return render(request, 'customuser_form.html', {'form': form})

class CustomUserListView(View):
    def get(self, request):
        users = CustomUser.objects.all()
        return render(request, 'customuser_list.html', {'users': users})

class ClienteCreateView(View):
    def get(self, request):
        form = ClienteForm()
        return render(request, 'cadastro_cliente.html', {'form': form})

    def post(self, request):
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.role = cliente.Role.CLIENTE

            # Define a senha do usuário
            password = form.cleaned_data['password']
            cliente.password = make_password(password)
            cliente.role = cliente.Role.CLIENTE
            cliente.save()


            cliente_profile, _= ClienteProfile.objects.get_or_create(user=cliente)
            cliente_profile.save()

            return redirect(reverse('locadora:pagina_principal'))
        
        return render(request, 'cadastro_cliente.html', {'form': form})

class ClienteListView(View):
    def get(self, request):
        clientes = Cliente.objects.all()
        return render(request, 'cliente_list.html', {'clientes': clientes})




#@login_and_role_required(roles=['ADMIN', 'FUNCIONARIO'])
class FuncionarioCreateView(View):
    def get(self, request):
        print(request.user.role)
        if request.user.role == 'CLIENTE': 
            return redirect(reverse('locadora:pagina_principal'))
        else:
            form = FuncionarioForm()
            return render(request, 'cadastro_funcionario.html', {'form': form})

    def post(self, request):
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.role = Funcionario.Role.FUNCIONARIO  # Define o papel como FUNCIONARIO

            # Define a senha do usuário
            password = form.cleaned_data['password']
            funcionario.password = make_password(password)
            funcionario.role = Funcionario.Role.FUNCIONARIO
            funcionario.save()

            funcionario_profile, _ = FuncionarioProfile.objects.get_or_create(user=funcionario)

            loja = form.cleaned_data['loja']
            funcionario_profile.loja = loja  # Atribui a loja ao FuncionarioProfile
            funcionario_profile.save()

            return redirect(reverse('locadora:pagina_principal'))
        return render(request, 'cadastro_funcionario.html', {'form': form})

class FuncionarioListView(View):
    def get(self, request):
        funcionarios = Funcionario.objects.all()
        return render(request, 'funcionario_list.html', {'funcionarios': funcionarios})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('locadora:pagina_principal')
            else:
                form.add_error(None, 'Invalid username or password')
        return render(request, 'login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('usuarios:login')