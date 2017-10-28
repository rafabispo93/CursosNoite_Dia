from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    carga_horaria = models.IntegerField()
    descricao = models.TextField()
    data_criacao = models.DateTimeField(
            default=timezone.now)
    data_publicacao= models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.data_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.nome
