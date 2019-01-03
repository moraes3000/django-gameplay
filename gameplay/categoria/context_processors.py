from .models import CategoriaModel,JogoModel


def categories(request):
    return {
        'categorias' : CategoriaModel.objects.all()

    }

def jogos(request):
    return {
        'jogos' : JogoModel.objects.all()

    }