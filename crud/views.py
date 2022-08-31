from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import tema
from .form import TemaForm

# Create your views here.

def create_tema(request):
    form = TemaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("listatemas")
    pacote = {"tema_form": form}
    return render(request, "temas.html", pacote)

def read_tema(request):
    temas = tema.objects.all()
    pacote = {"temaChaves" : temas}
    return render(request,  "temas.html", pacote)

def update_tema(request, id_tema):
    temas = tema.objects.get(pk = id_tema)
    form = TemaForm(request.POST or None, instance = temas)

    if form.is_valid():
        form.save()
        return redirect("listatemas")
    pacote = {"tema_form": form}

    return render(request, "editartemas.html", pacote)

def delete_tema(request, id_tema):
    temas = tema.objects.get(pk = id_tema)
    temas.delete()
    return redirect("lctemas.html")

def listar_noticias(request):
    return render(request,"listanoticias.html")