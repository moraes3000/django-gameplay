from django.shortcuts import render

# Create your views here.
from ..categoria.models import CategoriaModel

def home(request):
    # context = {
    #     'categorias' : CategoriaModel.objects.all()
    # }

    return render(request, 'index.html')