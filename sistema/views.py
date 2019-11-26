from django.shortcuts import render
from .models import Disciplina, Aluno, Professor

def alunos_list(request):
    alunos = Aluno.objects.all()
    disciplinas = Disciplina.objects.all()
    professores = Professor.objects.all()
    context = {
       'alunos_list': alunos,
       'turmas_list': disciplinas,
       'professores_list': professores

    }
    return render(request, 'sistema/list.html', context)
