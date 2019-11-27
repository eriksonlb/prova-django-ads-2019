from django.contrib import admin
from .models import Disciplina, Aluno, Professor, Matricula

@admin.register(Disciplina)
class disciplina_admin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'data_criacao']
    

@admin.register(Aluno)
class aluno_admin(admin.ModelAdmin):
    list_display = ['nome', 'matrícula', 'nota', 'faltas']

@admin.register(Professor)
class professor_admin(admin.ModelAdmin):
    list_display = ['nome', 'titulacao','endereço', 'telefone']

@admin.register(Matricula)
class professor_admin(admin.ModelAdmin):
    list_display = ['aluno']
