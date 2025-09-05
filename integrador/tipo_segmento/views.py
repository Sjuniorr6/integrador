from django.shortcuts import render, redirect
from .models import TipoSegmento
from .forms import TipoSegmentoForm

def listar_segmentos(request):
    segmentos = TipoSegmento.objects.all()
    return render(request, 'tipo_segmento/listar.html', {'segmentos': segmentos})

def criar_segmento(request):
    if request.method == 'POST':
        form = TipoSegmentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_segmentos')
    else:
        form = TipoSegmentoForm()
    return render(request, 'tipo_segmento/form.html', {'form': form})
