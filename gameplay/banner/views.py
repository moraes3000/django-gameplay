from django.shortcuts import render
from django.views.generic import ListView,CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
from .models import Banner, FotoBanner

# Banner
class BannerCreateView(CreateView):
    model = Banner
    fields = ['nome','intervalo', 'ocultartitulo','chave_estrangeira_jogo']


class BannerListView(ListView):
    model = Banner

class BannerDeleteView(DeleteView):
    model = Banner
    success_url = reverse_lazy('BannerListView')

class BannerUpdate(UpdateView):
    model = Banner
    fields = ['nome', 'intervalo', 'ocultartitulo', 'chave_estrangeira_jogo']

# FotoBanner

class FotoCreateView(CreateView):
    model = FotoBanner
    fields = ['nome', 'imagem','bannery','url','posicao','mostrartitulobanner']

class FotoBannerListView(ListView):
    model = FotoBanner

class FotorDelete(DeleteView):
    model = FotoBanner
    success_url = reverse_lazy('FotoBannerListView')

class FotoUpdate(UpdateView):
    model = FotoBanner
    fields = ['nome', 'imagem','bannery','url','posicao','mostrartitulobanner']
