from django.db import models
from datetime import datetime 

class Disciplina(models.Model):
	nome = models.CharField(max_length=30)
	data_criacao = models.DateTimeField(default=datetime.now, blank=True)
    
	def __str__(self):
		    return self.nome


class Aluno(models.Model):
	nome = models.CharField(max_length = 50)
	matrícula = models.CharField(max_length = 50, default='0')

	def __str__(self):
		    return self.nome

class Professor(models.Model):
	nome = models.CharField(max_length = 50)
	titulacao = models.CharField(max_length = 50, default='Titular')
	endereço = models.CharField(max_length = 50)
	telefone = models.CharField(max_length = 30)

	def __str__(self):
            return self.nome


class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    ano = models.IntegerField(default=2019)
    nota = models.CharField(max_length = 50, default='0')
    faltas = models.CharField(max_length = 50, default='0')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.aluno.nome

class Alocacao(models.Model):
    codigo = models.AutoField(primary_key=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    ano = models.IntegerField(default=2019)
    carga = models.IntegerField()
    horario = models.TimeField()

    def __str__(self):
        return self.professor.nome