from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

# models.py
from django.db import models
from datetime import date

class Registrar_serie_pelicula(models.Model):
    titulo_serie = models.CharField('Titulo Serie', max_length=120)
    fecha_serie = models.DateField('Fecha Serie')
    serie_o_pelicula = models.CharField('Serie/Pelicula', max_length=120)
    temporadas = models.IntegerField('Nº Temporadas',blank=True, null=True)
    episodios = models.IntegerField('Nº Episodios',blank=True, null=True)
    plataforma = models.CharField('Plataforma Serie', max_length=120)
    description = models.TextField('Description Serie', blank=True)
    genero = models.CharField('Género Serie', max_length=120)
    puntuacion = models.IntegerField('Puntuacion Serie (Del 1 al 10)')
    finalizada = models.BooleanField('Finalizada?', default=False)
    comentarios = models.TextField('Comentarios Serie', blank=True)
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
