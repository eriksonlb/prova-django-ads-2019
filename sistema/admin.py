from django.contrib import admin
from .models import Disciplina, Aluno, Professor

@admin.register(Disciplina)
class registro_ponto_admin(admin.ModelAdmin):
    list_display = ['nome', 'data_criacao']
    

@admin.register(Aluno)
class registro_ponto_admin(admin.ModelAdmin):
    list_display = ['nome', 'matrícula', 'nota', 'faltas']

@admin.register(Professor)
class registro_ponto_admin(admin.ModelAdmin):
    list_display = ['nome', 'titulacao','endereço', 'telefone']
