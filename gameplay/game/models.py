from django.urls import reverse

from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField

# Create your models here.

class Jogo(models.Model):
    nome = models.CharField(_("nome"), max_length=150)
    slug = models.SlugField(_("slug"), blank=True)
    descricao = RichTextField(u'Conteúdo', default='', blank=True, null=True)
    imagem = models.ImageField('Foto', upload_to="foto/post", default='', blank=True, null=True)
    criado = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['nome']

    def publish(self):
        self.criado = timezone.now()
        self.save()

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('AdminJogoListView')

    def generate_slug(self):
        from django.template.defaultfilters import slugify
        return slugify(self.nome)

@receiver(pre_save, sender=Jogo)
def my_handler(sender, instance, **kwargs):
    instance.slug = instance.generate_slug()


class Capitulo_jogo(models.Model):
    nome = models.CharField(_("nome"), max_length=150)
    slug = models.SlugField(_("slug"), blank=True)
    descricao = RichTextField(u'Conteúdo', default='', blank=True, null=True)
    imagem = models.ImageField('Foto', upload_to="foto/post", default='', blank=True, null=True)

    iframe = models.CharField(_("iframe url"), max_length=350, default='', blank=True, null=True)
    criado = models.DateTimeField(default=timezone.now)
    chave_estrangeira = models.ForeignKey("Jogo", verbose_name=_("jogo"), on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

    def generate_slug(self):
        from django.template.defaultfilters import slugify
        return slugify(self.nome)


    def get_absolute_url(self):
        return reverse('TodosCapitulosListView')