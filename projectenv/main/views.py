from django.db import models
from django.shortcuts import render
from django.http import request
from .models import PaintList, Paint

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
        'paints': paints
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
