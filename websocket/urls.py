from django.urls import path 
from . import views 

app_name = 'websocket'

urlpatterns = [
    path('sala/',views.salaView ,name='sala'),
    path('<slug>/', views.dashboard_aluguel, name='dashboard_aluguel'),
]
