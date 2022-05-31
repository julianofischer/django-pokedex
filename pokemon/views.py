from django.shortcuts import render
from pokemon.models import Pokemon, Tipo
from django.views.generic import ListView

class PokemonListView(ListView):
    model = Pokemon