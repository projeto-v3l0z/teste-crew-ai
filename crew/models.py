from django.db import models

# Create your models here.
class Pergunta(models.Model):
    pergunta = models.CharField(max_length=255)

    def __str__(self):
        return self.pergunta
    
class Vendas(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return self.resposta