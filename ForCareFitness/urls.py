from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ForCareFitnessApp import views

urlpatterns = [
    path('', views.cadastro, name='home'),  #
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('aluno/', views.aluno, name='aluno'),
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('admin/', views.admin, name='admin'),
    path('professor/', views.professor, name='professor'),
    path('fichas/', views.fichas, name='fichas'), 
    path('adicionar_fichas/', views.adicionar_fichas, name='adicionar_fichas'),
    path('remover_fichas/', views.remover_fichas, name='remover_fichas'),
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

