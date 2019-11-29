from django.contrib import admin
from .models import Disciplina, Aluno, Professor, Matricula, Alocacao

@admin.register(Disciplina)
class disciplina_admin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'data_criacao']
    

@admin.register(Aluno)
class aluno_admin(admin.ModelAdmin):
    list_display = ['nome', 'matrícula']

@admin.register(Professor)
class professor_admin(admin.ModelAdmin):
    list_display = ['nome', 'titulacao','endereço', 'telefone']

@admin.register(Matricula)
class professor_admin(admin.ModelAdmin):
    list_display = ['aluno', 'disciplina', 'nota', 'faltas', 'ano']
@admin.register(Alocacao)
class professor_admin(admin.ModelAdmin):
    list_display = ['codigo', 'professor', 'disciplina', 'ano', 'carga', 'horario']
