from django.shortcuts import render, redirect
from .models import Libro, Pelicula, Musica
from .forms import LibroFormulario, PeliculasFormulario, MusicaFormulario

def inicio(request):
    return render(request, "inicio.html")

def libros(request):
    libros = Libro.objects.all()
    return render(request, "libros.html", {"libros": libros})

def peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, "peliculas.html", {"peliculas": peliculas})

def musica(request):
    musica = Musica.objects.all()
    return render(request, "musica.html", {"musica": musica})

def guardar_objeto(request, form_class, template_name):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = form_class()
    return render(request, template_name, {"form": form})

def libro_formulario(request):
    return guardar_objeto(request, LibroFormulario, "libro_formulario.html")

def peliculas_formulario(request):
    return guardar_objeto(request, PeliculasFormulario, "pelicula_formulario.html")

def musica_formulario(request):
    return guardar_objeto(request, MusicaFormulario, "musica_formulario.html")

def busqueda_genero(request):
    return render(request, "busqueda_genero.html")

def buscar(request):
    genero = request.GET.get("genero", "")
    peliculas = Pelicula.objects.filter(genero__icontains=genero)
    return render(request, "resultados_busqueda.html", {"peliculas": peliculas, "genero": genero})
