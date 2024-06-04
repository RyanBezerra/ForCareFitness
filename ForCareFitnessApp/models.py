from django.db import models
class Usuario(models.Model):

    nome = models.CharField(max_length=100)
    nascimento = models.CharField()
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    senha = models.CharField(max_length=100)

class Fichas(models.Model):
    quantidade = models.CharField(max_length=100, default='0')

