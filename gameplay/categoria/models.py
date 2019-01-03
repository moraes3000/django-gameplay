from django.db import models

# Create your models here.

class CategoriaModel(models.Model):
    nome =  models.CharField(max_length=100)
    slug = models.SlugField('Nome da url', max_length=100)


    class Meta:
        verbose_name = 'Categoria'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class JogoModel(models.Model):
    nome =  models.CharField(max_length=100)
    slug = models.SlugField('Nome da url', max_length=100)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.CASCADE)
    descricao = models.TextField('Descrição', blank=True)


    class Meta:
        verbose_name = 'Jogo'
        ordering = ['nome']

    def __str__(self):
        return self.nome