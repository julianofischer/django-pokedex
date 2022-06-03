from django.contrib import admin
from pokemon import models

# Register your models here.
#admin.site.register(models.Pokemon)
#@admin.register(models.Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('nome', 'involucao', 'image_tag')
    # exclude = ('slug',)

admin.site.register(models.Pokemon, PokemonAdmin)
admin.site.register(models.Tipo)
