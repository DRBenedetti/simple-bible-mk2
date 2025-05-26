from django.shortcuts import render, get_object_or_404
from .models import Tema, Versiculo

def home(request):
    temas = Tema.objects.all()
    return render(request, 'home.html', {'temas': temas})


def tema(request, id):
    tema = get_object_or_404(Tema, id=id)
    versiculos = tema.versiculos.all()
    
    return render(request, 'versiculos.html', {'tema': tema, 'versiculos': versiculos})
