from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import noticia, tema
from .form import NoticiaForm, TemaForm

# Create your views here.
def read_tema(request):
    form = TemaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("listatemas")
    temas = tema.objects.all()
    pacote = {"temaChaves" : temas, "tema_form": form, }
    return render(request,  "lctemas.html", pacote)

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
    return redirect("listatemas")

def read_noticia(request):
    form = NoticiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("listanoticias")
    noticias = noticia.objects.all()
    pacote = {"noticiaChaves" : noticias, "noticia_form": form}
    return render(request,  "listanoticias.html", pacote)

def update_noticia(request, id_noticia):
    noticias = noticia.objects.get(pk = id_noticia)
    form = NoticiaForm(request.POST or None, instance = noticias)

    if form.is_valid():
        form.save()
        return redirect("listanoticias")
    pacote = {"noticia_form": form}
    return render(request, "editar_noticia.html", pacote)

def delete_noticia(request, id_noticia):
    noticias = noticia.objects.get(pk = id_noticia)
    noticias.delete()
    return redirect("listanoticias")

