from django.db import models

# Create your models here.
from django.urls import reverse
from gameplay.game.models import Jogo

class Banner(models.Model):
    nome = models.CharField("nome", max_length=150)
    slug = models.SlugField("slug", blank=True)
    intervalo = models.IntegerField('Digite o intervalo em que o banner irá deslizar em milisegundos', default=4500,
                                    blank=True, null=True)
    ocultartitulo = models.BooleanField('Marque para ocultar o título do banner', default=False)
    chave_estrangeira_jogo = models.ForeignKey("game.Jogo", on_delete=models.CASCADE)


    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('BannerListView')

    def generate_slug(self):
        from django.template.defaultfilters import slugify
        return slugify(self.nome)


class FotoBanner(models.Model):
    nome = models.CharField(u'Nome', max_length=100, default='', blank=True, null=True)
    imagem = models.ImageField(u'Imagem do banner', upload_to="photo/banner", default='', blank=True, null=True)
    bannery = models.ForeignKey("Banner", verbose_name='Banner JOGOl', on_delete=models.CASCADE)
    url = models.CharField('Digite uma URL para a imagem', max_length=200, default='', blank=True, null=True)
    posicao = models.IntegerField(default=0, blank=True, null=True)
    mostrartitulobanner = models.BooleanField('Marque para ocultar o título do banner', default=False)



    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('FotoBannerListView')