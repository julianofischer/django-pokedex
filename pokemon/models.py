from django.db import models
from colorfield.fields import ColorField

# Create your models here.
class Pokemon(models.Model):
    nome = models.CharField(max_length=200)
    ataque = models.PositiveSmallIntegerField()
    defesa = models.PositiveSmallIntegerField()
    stamina = models.PositiveSmallIntegerField()
    involucao = models.ForeignKey('self', on_delete=models.CASCADE, related_name='evolucoes', null=True, blank=True)
    foto = models.ImageField(upload_to='media')
    tipos = models.ManyToManyField('Tipo', blank=True)

    def __str__(self):
        return self.nome
    
    def image_tag(self):
        from django.utils.html import escape, mark_safe
        return mark_safe(f'<img style="width:64px;height:64px;" src=/media/{escape(self.foto)}>')

    image_tag.short_description = 'Image'


class Tipo(models.Model):
    nome = models.CharField(max_length=100)
    forcas = models.ManyToManyField('self',
        blank=True,
        symmetrical=False,
        verbose_name='Forças',
        related_name='fraco_contra')
    
    fraquezas = models.ManyToManyField('self',
        blank=True,
        symmetrical=False,
        verbose_name='Fraquezas',
        related_name='forte_contra')

    cor = ColorField(default="#FFFFFF")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering =['nome']
    
