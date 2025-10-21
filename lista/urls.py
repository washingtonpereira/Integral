from django.urls import path

from . import views

urlpatterns = [
   
    path('listas', views.home_list,name='listagem'),
    path('', views.index , name='home'),
    path('listas/cadastro/', views.cadastro, name='cadastro_listas'),


]
