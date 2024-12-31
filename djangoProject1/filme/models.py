from django.db import models
from django.utils import timezone
# Create your models here.

#Criar Filme

#O nome da variável está em maiúsculo pois é uma constante.
#O que vai na tupla é ("banco de dados", "aparece para o user")
LISTA_CATEGORIAS = (
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros")
)
class Filme(models.Model):
    thumb = models.ImageField(upload_to='thumb_filmes')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)