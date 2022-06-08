"""pokedex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pokemon.views import PokemonListView, TipoListView,\
    PokemonDetailView, PokemonEvolutionsListView, \
    PokemonInvolutionListView, PokemonPorTipoListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokemons/', PokemonListView.as_view()),
    path('pokemons/tipos/', TipoListView.as_view()),
    path('pokemons/tipos/<str:nome>/', PokemonPorTipoListView.as_view(), name='pokemon_tipo_list'),
    path('pokemons/<slug:slug>/', PokemonDetailView.as_view(), name='pokemon_detail'),
    path('pokemons/<slug:slug>/evolucoes/', PokemonEvolutionsListView.as_view(), name='pokemon_evo_list'),
    path('pokemons/<slug:slug>/involucao/', PokemonInvolutionListView.as_view(), name='pokemon_invo_list'),
    path('pokemons/<int:pk>', PokemonDetailView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, 
document_root=settings.MEDIA_ROOT)
