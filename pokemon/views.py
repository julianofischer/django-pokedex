from django.shortcuts import render
from pokemon.models import Pokemon, Tipo
from django.views.generic import ListView, DetailView

class PokemonListView(ListView):
    model = Pokemon 

class PokemonEvolutionsListView(ListView):
    model = Pokemon
    def get_queryset(self):
        qs = super().get_queryset() 
        slug = self.kwargs['slug']
        p = Pokemon.objects.get(slug=slug)
        qs = qs.filter(involucao__pk=p.pk)
        print(qs)
        return qs

class PokemonInvolutionListView(DetailView):
    model = Pokemon
    def get_object(self):
        slug = self.kwargs['slug']
        p = Pokemon.objects.get(slug=slug)
        return p.involucao

class PokemonPorTipoListView(ListView):
    model = Pokemon
    def get_queryset(self):
        qs = super().get_queryset() 
        nome = self.kwargs['nome'].capitalize()
        t = Tipo.objects.get(nome=nome)
        qs = qs.filter(tipos=t)
        return qs

class PokemonDetailView(DetailView):
    model = Pokemon 

class TipoListView(ListView):
    model = Tipo