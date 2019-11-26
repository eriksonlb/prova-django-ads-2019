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
	nota = models.CharField(max_length = 50, default='0')
	faltas = models.CharField(max_length = 50, default='0')

	def __str__(self):
		    return self.nome

class Professor(models.Model):
	disciplina = models.ManyToManyField(Disciplina)
	nome = models.CharField(max_length = 50)
	titulacao = models.CharField(max_length = 50, default='titular')
	endereço = models.CharField(max_length = 50, default='0')
	telefone = models.CharField(max_length = 30, default='0')

	def __str__(self):
            return self.nome