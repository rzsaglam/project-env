from django import forms
from django.contrib.auth.views import redirect_to_login
from django.db import models
from django.shortcuts import redirect, render
from django.http import request
from django.urls import reverse
from .models import Paint
from .forms import PaintForm, StockForm, NewUserForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
# Create your views here.


def index(request):
    paints = Paint.objects.all()
    context = {
        'paints': paints,
    }
    return render(request, 'pages/index.html', context,)


def ferropox(request):
    paints = Paint.objects.filter(
        name="Ferropox", location="İstanbul", weight="20 KG")
    paints2 = Paint.objects.filter(
        name="Ferropox", location="İstanbul", weight="5 KG")
    context = {
        'paints': paints,
        'paints2': paints2,
    }
    return render(request, 'pages/ferropox.html', context)


def alkid(request):
    paints = Paint.objects.filter(
        name="Alkid", location="İstanbul", weight="20 KG")
    paints2 = Paint.objects.filter(
        name="Alkid", location="İstanbul", weight="5 KG")
    context = {
        'paints': paints,
        'paints2': paints2,
    }
    return render(request, 'pages/alkid.html', context)


def promega(request):
    paints = Paint.objects.filter(
        name="Promega", location="İstanbul", weight="20 KG")
    paints2 = Paint.objects.filter(
        name="Promega", location="İstanbul", weight="5 KG")
    context = {
        'paints': paints,
        'paints2': paints2,
    }
    return render(request, 'pages/promega.html', context)


def big_paints(request):
    paints = Paint.objects.filter(location="Yalova", weight="20 KG")
    context = {
        'paints': paints,
    }
    return render(request, 'pages/buyuk-boyalar.html', context)


def alkid_yalova(request):
    paints = Paint.objects.filter(
        name="Alkid", location="Yalova", weight="20 KG")
    paints2 = Paint.objects.filter(
        name="Alkid", location="Yalova", weight="5 KG")
    context = {
        'paints': paints,
        'paints2': paints2,
    }
    return render(request, 'pages/alkid-yalova.html', context)


def promega_yalova(request):
    paints = Paint.objects.filter(
        name="Promega", location="Yalova", weight="20 KG")
    paints2 = Paint.objects.filter(
        name="Promega", location="Yalova", weight="5 KG")
    context = {
        'paints': paints,
        'paints2': paints2,
    }
    return render(request, 'pages/promega-yalova.html', context)


def addPaint(request):
    paintForm = PaintForm(request.POST)
    if paintForm.is_valid():
        paintForm.save()
        messages.success(request, "Başarıyla Eklendi.")
    return render(request, 'pages/boya-ekle.html', {"paintForm": paintForm})


def editPaint(request, id):
    if request.user.is_authenticated:
        paint = Paint.objects.get(id=id)
        return render(request, "pages/edit.html", {"paint": paint})


def updatePaint(request, id):
    paint = Paint.objects.get(id=id)
    form = StockForm(request.POST, instance=paint)
    if form.is_valid():
        form.save()
        messages.success(request, "Başarıyla Güncellendi.")
        return render(request, "pages/edit.html", {"paint": paint})


def loginView(request):
    form = LoginForm()
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, "Başarılı")
        return redirect_to_login("accounts/profile.html")
    else:
        messages.warning(request, "Başarısız")

    return render(request, "accounts/login.html", {'form': form})


def logoutView(request):
    if logout(request):
        return render(request, "accounts/logout.html")


def profile(request):
    return render(request, 'accounts/profile.html')
# def register(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful.")
#             return redirect('alkid')
#         messages.error(
#             request, "Unsuccessful registration. Invalid information.")
#     form = NewUserForm
#     return render(request, "pages/register.html", {"form": form})
