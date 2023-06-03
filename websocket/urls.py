from django.urls import path 
from . import views 

app_name = 'websocket'

urlpatterns = [
    path('sala/',views.salaView ,name='sala'),
    path('<slug>/', views.dashboard_aluguel, name='dashboard_aluguel'), # WEBSOCKET 
    path('redirect_dashboard/', views.redirecionar_dashboard, name='redirect_dashboard') 
]
