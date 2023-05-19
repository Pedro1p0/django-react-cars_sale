# urls.py
from django.urls import path
from .views import CustomUserCreateView, CustomUserListView, ClienteCreateView, ClienteListView, FuncionarioCreateView, FuncionarioListView,LoginView, LogoutView


app_name = "usuarios"

urlpatterns = [
    path('customuser/create/', CustomUserCreateView.as_view(), name='customuser-create'),
    path('customuser/', CustomUserListView.as_view(), name='customuser-list'),
    path('cliente/create/', ClienteCreateView.as_view(), name='cliente-create'),
    path('cliente/', ClienteListView.as_view(), name='cliente-list'),
    path('funcionario/create/', FuncionarioCreateView.as_view(), name='funcionario-create'),
    path('funcionario/', FuncionarioListView.as_view(), name='funcionario-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
