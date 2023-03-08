from dataclasses import fields
from django import forms
from .models import Usuario
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'email', 'nome', 'idade', 'cpf']    