from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, fields
from .models import Paint


class StockForm(forms.ModelForm):
    class Meta:
        model = Paint
        fields = "__all__"
