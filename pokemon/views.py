from django.shortcuts import render
from pokemon.models import Pokemon, Tipo
from django.views.generic import ListView, DetailView

class PokemonListView(ListView):
    model = Pokemon 

class PokemonDetailView(DetailView):
    model = Pokemon 

class TipoListView(ListView):
    model = Tipo