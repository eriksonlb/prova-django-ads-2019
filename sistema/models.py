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
	ano_letivo = models.IntegerField( default=f'{datetime.now().year}')
	nota = models.CharField(max_length = 50, default='0')
	faltas = models.CharField(max_length = 50, default='0')

	def __str__(self):
		    return self.nome

class Professor(models.Model):
	disciplina = models.ManyToManyField(Disciplina)
	nome = models.CharField(max_length = 50)
	titulacao = models.CharField(max_length = 50, default='Titular')
	endereço = models.CharField(max_length = 50)
	telefone = models.CharField(max_length = 30)

	def __str__(self):
            return self.nome


class Matricula(models.Model):
	disciplina = models.ManyToManyField(Disciplina)
	aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE, default=0)
	data_criacao = models.DateTimeField(default=datetime.now().year, blank=True)

	def __str__(self):
            return self.nome