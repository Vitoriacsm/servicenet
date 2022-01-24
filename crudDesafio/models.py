from django.db import models


# Create your models here.

class UsuariosMedicos(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=30, blank=True, null=True)
    senha = models.CharField(max_length=20, blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)


class ClientesPacientes(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=13, blank=True, null=True)
    endereco = models.CharField(max_length=30, blank=True, null=True)
    numero = models.CharField(max_length=5, blank=True, null=True)
    cidade = models.CharField(max_length=20, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    pais = models.CharField(max_length=20, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    data_criacao = models.DateTimeField(blank=True, null=True)

class Agendamento(models.Model):
    data = models.DateTimeField(blank=True, null=True)
    descricao = models.TextField()
    status = models.CharField(max_length=100)




