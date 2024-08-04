import calendar
import datetime
from calendar import HTMLCalendar
from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import csv
from django.http import FileResponse
import io
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . forms import RegisterUserForm
from .forms import RegistrarSeriePeliculaForm
from .models import Registrar_serie_pelicula
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
import mimetypes

# Create your views here.

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "John"
    name = request.user.username
    month = month.capitalize()
    day = datetime.today()
    
    # convert month name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
       
    # create calendar
    cal = calendar.HTMLCalendar().formatmonth(year, month_number)
    # create current year
    now = datetime.now()
    current_year = now.year

    # query event date
        
    time = now.strftime('%I:%M:%S %p')

    context = {"name": name, "year": year, "month": month, "month_number": month_number, "cal": cal, "current_year": current_year, "time": time, "day":day}
    return render(request, 'series_peliculas_app/home.html', context)



def login_user(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, "Error during login prueba oitra vez")
            return redirect('login')
    else:
        context = {}
        return render(request, 'series_peliculas_app/login.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, "you were logged out")
    return redirect('home')

def register_user(request):
    
    if request.method == "POST":
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            
            user = authenticate(username=username, password=password)
            
            login(request,user)
            
            messages.success(request, "registracion successfull")
            return redirect('home')
    else:
        form=RegisterUserForm()
    
    
    context={'form':form}
    return render(request, 'series_peliculas_app/register_user.html', context)


def registrar_serie_pelicula_view(request):
    if request.method == 'POST':
        form = RegistrarSeriePeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            #titulo_serie = request.POST['titulo_serie']
            #serie_o_pelicula = request.POST['serie_o_pelicula']
            #plataforma = request.POST['plataforma']
            #name = request.user.username
            #file = request.FILES['file']
            instance = form.save()
            titulo_serie = instance.titulo_serie
            serie_o_pelicula = instance.serie_o_pelicula
            plataforma = instance.plataforma
            name = request.user.username
            serie_pelicula_imagen = instance.serie_pelicula_imagen
            #files = request.FILES.getlist('files')
            email_message = EmailMessage(
                subject=f'Contact Form: {name} - {titulo_serie}',
                #body=titulo_serie + " " + serie_o_pelicula + " " +  plataforma,
                body=f'Titulo: {titulo_serie}\nTipo: {serie_o_pelicula}\nPlataforma: {plataforma}',
                
                from_email=settings.EMAIL_HOST_USER,
                to=['msb.duck@gmail.com', 'msb.tesla@gmail.com', 'msebti2@gmail.com', 'msb.acer@gmail.com'],
                reply_to=['msebti2@gmail.com']
            )
            # Adjuntar cada archivo
            #for file in files:
                #email_message.attach(file.name, file.read(), file.content_type)
            
            if serie_pelicula_imagen:
                mime_type, _ = mimetypes.guess_type(serie_pelicula_imagen.path)
                email_message.attach(serie_pelicula_imagen.name, serie_pelicula_imagen.read(), mime_type)
            
            # Adjuntar el archivo
            #email_message.attach(file.name, file.read(), file.content_type)

            # Enviar el email
            email_message.send(fail_silently=False)
            form.save()
            return redirect('lista_series_peliculas')  # Cambia esto por la vista a la que deseas redirigir después de guardar
    else:
        form = RegistrarSeriePeliculaForm()
    return render(request, 'crear_serie_pelicula.html', {'form': form})


def lista_series_peliculas(request):
    # venue_list = Venue.objects.all().order_by('?')
    la_lista_de_series_peliculas = Registrar_serie_pelicula.objects.all()
    name = request.user.username
    # set pagination
    
    p = Paginator(la_lista_de_series_peliculas, 2)
    page = request.GET.get('page')
    todas_series_peliculas = p.get_page(page)
    nums = "a" * todas_series_peliculas.paginator.num_pages
    
    print("hola : " + str(todas_series_peliculas.paginator.num_pages))
    
    context = {'la_lista_de_series_peliculas': la_lista_de_series_peliculas, 'todas_series_peliculas': todas_series_peliculas, 'nums': nums, 'name':name}
    return render(request, 'series_peliculas_app/toda_lalista_series_peliculas.html', context)

def actualizar_serie_pelicula(request, id_serie_pelicula):
    serie_pelicula = Registrar_serie_pelicula.objects.get(pk=id_serie_pelicula)
    form = RegistrarSeriePeliculaForm(request.POST or None, request.FILES or None,  instance=serie_pelicula)
    if form.is_valid():
        form.save()
        return redirect('lista_series_peliculas')
    context = {'serie_pelicula': serie_pelicula, 'form': form}
    return render(request, 'series_peliculas_app/actualizar_serie_pelicula.html', context)

def eliminar_serie_pelicula2(request, id_serie_pelicula):
    venue = Registrar_serie_pelicula.objects.get(pk=id_serie_pelicula)
    venue.delete()
    return redirect('lista_series_peliculas')

def eliminar_serie_pelicula(request, id_serie_pelicula):
    la_serie_pelicula = get_object_or_404(Registrar_serie_pelicula, id=id_serie_pelicula)
    la_serie_pelicula.delete()
    messages.success(request, "La serie o película ha sido eliminada con éxito.")
    return redirect('lista_series_peliculas')  # Reemplaza 'nombre_de_tu_vista' con el nombre de tu vista principal