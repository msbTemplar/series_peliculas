from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Registrar_serie_pelicula #, Genero
from django.core.validators import MinValueValidator, MaxValueValidator

class RegisterUserForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
    
    def __init__(self, *args, **kwargs) :
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
        

class RegistrarSeriePeliculaForm(forms.ModelForm):
    class Meta:
        model = Registrar_serie_pelicula
        fields = '__all__'
        widgets = {
            'titulo_serie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo Serie','name':'titulo_serie'}),
            #'fecha_serie': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha Serie' , 'type': 'date'}),
            #'fecha_serie': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Año de la Serie', 'min': '1900', 'max': '2100', 'id':'id_fecha_serie'}),
            'fecha_serie': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Año de la Serie', 'min': '1900', 'max': '2100', 'id':'id_fecha_serie'}),
            #'serie_o_pelicula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Serie/Película', 'id':'id_serie_o_pelicula','name':'serie_o_pelicula'}),
            'serie_o_pelicula': forms.Select(attrs={'class': 'form-control'}, choices=Registrar_serie_pelicula.SERIE_PELICULA_CHOICES),
            'temporadas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nº Temporadas', 'id':'id_temporadas'}),
            'episodios': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nº Episodios', 'id':'id_episodios'}),
            'plataforma': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Plataforma Serie','name':'plataforma'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción Serie'}),
            #'genero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Género Serie'}),
            'genero': forms.Select(attrs={'class': 'form-control'}, choices=Registrar_serie_pelicula.GENERO_CHOICES),
            #'puntuacion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Puntuación Serie', 'min' : 1, 'max' : 10}),
            'puntuacion': forms.Select(attrs={'class': 'form-control'}, choices=Registrar_serie_pelicula.PUNTUACION_CHOICES),
            'finalizada': forms.CheckboxInput(attrs={'class': 'form-check-input','id':'id_finalizada'}),
            'comentarios': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comentarios Serie'}),
            'serie_pelicula_imagen': forms.ClearableFileInput(attrs={'class': 'form-control', 'name':'files' ,'id':'formFile', 'type':'file'}),
            'recomendado_por': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recomendado Por'}),
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['serie_o_pelicula'].widget.attrs['disabled'] = True  # Desactivar el campo por defecto
            
        def clean(self):
            cleaned_data = super().clean()
            serie_o_pelicula = cleaned_data.get("serie_o_pelicula")
            temporadas = cleaned_data.get("temporadas")
            episodios = cleaned_data.get("episodios")

            if serie_o_pelicula == "Serie":
                if not temporadas:
                    self.add_error('temporadas', "Este campo es obligatorio para una serie.")
                if not episodios:
                    self.add_error('episodios', "Este campo es obligatorio para una serie.")
        
            return cleaned_data
