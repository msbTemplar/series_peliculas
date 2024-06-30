from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

# models.py
from django.db import models
from datetime import date
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class Registrar_serie_pelicula(models.Model):
    SERIE_PELICULA_CHOICES = [
        ('Serie', 'Serie'),
        ('Pelicula', 'Película')
    ]
    GENERO_CHOICES = [
        ('Drama', 'Drama'),
        ('Comedia', 'Comedia'),
        ('Ciencia ficción', 'Ciencia ficción'),
        ('Fantasía', 'Fantasía'),
        ('Acción', 'Acción'),
        ('Terror', 'Terror'),
        ('Aventura', 'Aventura'),
        ('Thriller', 'Thriller'),
        ('Policial', 'Policial'),
        ('Histórica', 'Histórica'),
        ('Animación', 'Animación'),
        ('Romance', 'Romance'),
        ('Documental', 'Documental'),
        ('Musical', 'Musical'),
        ('Western', 'Western'),
        ('Guerra', 'Guerra'),
         ('Biográfica', 'Biográfica'),
        ('Cine negro', 'Cine negro'),
        ('Cine experimental:', 'Cine experimental:'),
        ('Cine de arte', 'Cine de arte')
    ]
    
    PUNTUACION_CHOICES = [(i, str(i)) for i in range(1, 11)]
    serie_o_pelicula = models.CharField('Serie/Pelicula', max_length=120, choices=SERIE_PELICULA_CHOICES)
    titulo_serie = models.CharField('Titulo', max_length=120)
    fecha_serie = models.IntegerField('Año')
    #serie_o_pelicula = models.CharField('Serie/Pelicula', max_length=120)
    #serie_o_pelicula = models.CharField('Serie/Pelicula', max_length=120, choices=SERIE_PELICULA_CHOICES)
    temporadas = models.IntegerField('Nº Temporadas',blank=True, null=True)
    episodios = models.IntegerField('Nº Episodios',blank=True, null=True)
    plataforma = models.CharField('Plataforma', max_length=120)
    description = models.TextField('Description', blank=True)
    #genero = models.CharField('Género', max_length=120)
    genero = models.CharField('Género', max_length=120, choices=GENERO_CHOICES)
    #puntuacion = models.IntegerField('Puntuacion Serie (Del 1 al 10)')
    puntuacion = models.IntegerField('Puntuacion (Del 1 al 10)', choices=PUNTUACION_CHOICES)
    finalizada = models.BooleanField('Finalizada?', default=False)
    comentarios = models.TextField('Comentarios', blank=True)
    serie_pelicula_imagen = models.ImageField(null=True, blank=True, upload_to="images/")
    recomendado_por = models.CharField('Recomendado Por', max_length=120)

    def __str__(self) -> str:
        return self.titulo_serie + " - " + self.description

    @property
    def Days_till(self):
        today = date.today()
        days_till = self.fecha_serie.date() - today
        days_til_stripped = str(days_till).split(",", 1)[0]
        return days_til_stripped

    @property
    def Is_Past(self):
        today = date.today()
        if self.fecha_serie.date() < today:
            return "Past"
        else:
            return "Future"
