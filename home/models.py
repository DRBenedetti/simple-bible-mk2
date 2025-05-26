from django.db import models

class Tema(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Versiculo(models.Model):
    referencia = models.CharField(max_length=100)
    texto = models.TextField()
    temas = models.ManyToManyField(Tema, related_name='versiculos')

    def __str__(self):
        return self.referencia
