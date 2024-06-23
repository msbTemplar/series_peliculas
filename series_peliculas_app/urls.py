"""
URL configuration for series_peliculas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

from django.urls import path
from .views import registrar_serie_pelicula_view

urlpatterns = [
    path('', views.home, name='home'),
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('registrar_serie_pelicula/', registrar_serie_pelicula_view, name='registrar_serie_pelicula'),
    path('lista_series_peliculas', views.lista_series_peliculas, name='lista_series_peliculas'),
    path('actualizar_serie_pelicula/<id_serie_pelicula>', views.actualizar_serie_pelicula, name='actualizar_serie_pelicula'),
    path('eliminar_serie_pelicula/<id_serie_pelicula>', views.eliminar_serie_pelicula, name='eliminar_serie_pelicula'),
]
