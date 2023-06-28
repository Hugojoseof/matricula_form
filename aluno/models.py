from django.db import models

# Create your models here.
class Cidade (models.Model):
    nome = models.CharField(max_length= 100)
    sigla_estado = models.CharField(max_length=2)

class Curso(models.Model):
    nome = models.CharField(max_length=100)

class Matricula(models.Model):
    nome_aluno = models.CharField(max_length=150)
    endereco = models.CharField(max_length=250)
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    
