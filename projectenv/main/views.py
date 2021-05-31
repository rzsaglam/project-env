import re
from django import forms
from django.db import models
from django.shortcuts import redirect, render
from django.http import request
from .models import Paint
from .forms import StockForm
from django.contrib import messages
# Create your views here.


def index(request):
    paints = Paint.objects.all()
    context = {
        'paints': paints,
    }
    return render(request, 'pages/index.html', context,)


def ferropox(request):
    paints = Paint.objects.filter(name="Ferropox")
    context = {
        'paints': paints,
    }
    return render(request, 'pages/ferropox.html', context)


def alkid(request):
    paints = Paint.objects.filter(name="Alkid")
    context = {
        'paints': paints,
    }
    return render(request, 'pages/alkid.html', context)


def promega(request):
    paints = Paint.objects.filter(name="Promega")
    context = {
        'paints': paints
    }
    return render(request, 'pages/promega.html', context)


def editPaint(request, id):
    paint = Paint.objects.get(id=id)
    return render(request, "pages/edit.html", {"paint": paint})


def updatePaint(request, id):
    paint = Paint.objects.get(id=id)
    form = StockForm(request.POST, instance=paint)
    if form.is_valid():
        form.save()
        messages.success(request, "Başarıyla Güncellendi.")
        return render(request, "pages/edit.html", {"paint": paint})
