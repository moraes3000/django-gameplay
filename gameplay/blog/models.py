from django.urls import reverse

from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField

from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField

from django.utils import timezone

# Create your models here.

class Post(models.Model):
    nome = models.CharField(_("nome"), max_length=150)
    sumario = models.CharField("Escreva o conteúdo no máximo 150 caracteres", max_length=150, blank=True, null=True)
    slug = models.SlugField(_("slug"), blank=True)
    descricao = RichTextField(u'Conteúdo', default='', blank=True, null=True)
    imagem = models.ImageField('Foto', upload_to="foto/post", default='', blank=True, null=True)
    criado = models.DateTimeField(default=timezone.now)
    # #para o ckeditor

    class Meta:
        ordering = ['-criado']

    def publish(self):
        self.criado = timezone.now()
        self.save()

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('PostListView')

    def generate_slug(self):
        from django.template.defaultfilters import slugify
        return slugify(self.nome)



@receiver(pre_save, sender=Post)
def my_handler(sender, instance, **kwargs):
    instance.slug = instance.generate_slug()
