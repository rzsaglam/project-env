from django import forms
from django.contrib.auth import models
from django.db.models.base import Model
from django.forms import ModelForm, fields
from .models import Paint
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class StockForm(forms.ModelForm):
    class Meta:
        model = Paint
        fields = "__all__"


class PaintForm(forms.ModelForm):
    class Meta:
        model = Paint
        fields = "__all__"

    def save(self, commit=True):
        paint = super(PaintForm, self).save(commit=False)
        if commit:
            paint.save()
        return paint


class NewUserForm(UserCreationForm):
    username = forms.CharField(max_length=200, required=True, widget=forms.TextInput(
        attrs={'class': 'input-group-text'}))

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=200, required=True, widget=forms.TextInput(
        attrs={'class': 'input-group-text'}))
    password = forms.CharField(max_length=200, required=True, widget=forms.TextInput(
        attrs={'class': 'input-group-text'}))

    class Meta:
        model = User
        fields = ("username", "password")
