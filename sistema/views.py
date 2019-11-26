from django.shortcuts import render
from .models import Turma, Aluno, Professor

def alunos_list(request):
    alunos = Aluno.objects.all()
    turmas = Turma.objects.all()
    professores = Professor.objects.all()
    context = {
       'alunos_list': alunos,
       'turmas_list': turmas,
       'professores_list': professores

    }
    return render(request, 'sistema/list.html', context)
