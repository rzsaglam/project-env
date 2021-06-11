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
    return render(request, 'pages/index.html')


def big_paints_istanbul(request):
    alkid = Paint.objects.filter(
        name="Alkid", location="İstanbul", weight="20 KG", choice="Boya")
    ferropox = Paint.objects.filter(
        name="Ferropox", location="İstanbul", weight="20 KG", choice="Boya")
    promega = Paint.objects.filter(
        name="Promega", location="İstanbul", weight="20 KG", choice="Boya")
    ferromel = Paint.objects.filter(
        name="Ferromel", location="İstanbul", weight="20 KG", choice="Boya")
    epoxy = Paint.objects.filter(
        name="Epoxy", location="İstanbul", weight="20 KG", choice="Boya")
    akrilik = Paint.objects.filter(
        name="Akrilik", location="İstanbul", weight="20 KG", choice="Boya")
    promarin = Paint.objects.filter(
        name="Promarin", location="İstanbul", weight="20 KG", choice="Boya")
    underwater = Paint.objects.filter(
        name="Under Water", location="İstanbul", weight="20 KG", choice="Boya")
    ferforje = Paint.objects.filter(
        name="Ferforje", location="İstanbul", weight="20 KG", choice="Boya")
    antipas = Paint.objects.filter(
        name="Anti Pas", location="İstanbul", weight="20 KG", choice="Boya")
    aluminyum = Paint.objects.filter(
        name="Aluminyum", location="İstanbul", weight="20 KG", choice="Boya")
    resistant = Paint.objects.filter(
        name="Isıya Dayanıklı", location="İstanbul", weight="20 KG", choice="Boya")
    context = {
        'alkid': alkid,
        'ferropox': ferropox,
        'promega': promega,
        'ferromel': ferromel,
        'epoxy': epoxy,
        'akrilik': akrilik,
        'promarin': promarin,
        'underwater': underwater,
        'ferforje': ferforje,
        'antipas': antipas,
        'aluminyum': aluminyum,
        'resistant': resistant,
    }
    return render(request, 'pages/buyuk-boyalar-istanbul.html', context)


def small_paints_istanbul(request):
    alkid = Paint.objects.filter(
        name="Alkid", location="İstanbul", weight="5 KG", choice="Boya")
    ferropox = Paint.objects.filter(
        name="Ferropox", location="İstanbul", weight="5 KG", choice="Boya")
    promega = Paint.objects.filter(
        name="Promega", location="İstanbul", weight="5 KG", choice="Boya")
    ferromel = Paint.objects.filter(
        name="Ferromel", location="İstanbul", weight="5 KG", choice="Boya")
    epoxy = Paint.objects.filter(
        name="Epoxy", location="İstanbul", weight="5 KG", choice="Boya")
    akrilik = Paint.objects.filter(
        name="Akrilik", location="İstanbul", weight="5 KG", choice="Boya")
    promarin = Paint.objects.filter(
        name="Promarin", location="İstanbul", weight="5 KG", choice="Boya")
    underwater = Paint.objects.filter(
        name="Under Water", location="İstanbul", weight="5 KG", choice="Boya")
    ferforje = Paint.objects.filter(
        name="Ferforje", location="İstanbul", weight="5 KG", choice="Boya")
    antipas = Paint.objects.filter(
        name="Anti Pas", location="İstanbul", weight="5 KG", choice="Boya")
    aluminyum = Paint.objects.filter(
        name="Aluminyum", location="İstanbul", weight="5 KG", choice="Boya")
    resistant = Paint.objects.filter(
        name="Isıya Dayanıklı", location="İstanbul", weight="5 KG", choice="Boya")
    context = {
        'alkid': alkid,
        'ferropox': ferropox,
        'promega': promega,
        'ferromel': ferromel,
        'epoxy': epoxy,
        'akrilik': akrilik,
        'promarin': promarin,
        'underwater': underwater,
        'ferforje': ferforje,
        'antipas': antipas,
        'aluminyum': aluminyum,
        'resistant': resistant,
    }
    return render(request, 'pages/kucuk-boyalar-istanbul.html', context)


def thinners_istanbul(request):
    epoxy20 = Paint.objects.filter(
        name="Epoxy", location="İstanbul", weight="20 KG", choice="Tiner")
    epoxy12 = Paint.objects.filter(
        name="Epoxy", location="İstanbul", weight="12 KG", choice="Tiner")
    epoxy5 = Paint.objects.filter(
        name="Epoxy", location="İstanbul", weight="5 KG", choice="Tiner")
    polyurethane20 = Paint.objects.filter(
        name="Polyurethane", location="İstanbul", weight="20 KG", choice="Tiner")
    polyurethane12 = Paint.objects.filter(
        name="Polyurethane", location="İstanbul", weight="12 KG", choice="Tiner")
    polyurethane5 = Paint.objects.filter(
        name="Polyurethane", location="İstanbul", weight="5 KG", choice="Tiner")
    zehirli20 = Paint.objects.filter(
        name="Zehirli", location="İstanbul", weight="20 KG", choice="Tiner")
    zehirli12 = Paint.objects.filter(
        name="Zehirli", location="İstanbul", weight="12 KG", choice="Tiner")
    zehirli5 = Paint.objects.filter(
        name="Zehirli", location="İstanbul", weight="5 KG", choice="Tiner")
    sentetik20 = Paint.objects.filter(
        name="Sentetik", location="İstanbul", weight="20 KG", choice="Tiner")
    sentetik12 = Paint.objects.filter(
        name="Sentetik", location="İstanbul", weight="12 KG", choice="Tiner")
    sentetik5 = Paint.objects.filter(
        name="Sentetik", location="İstanbul", weight="5 KG", choice="Tiner")
    selulozik20 = Paint.objects.filter(
        name="Selulozik", location="İstanbul", weight="20 KG", choice="Tiner")
    selulozik12 = Paint.objects.filter(
        name="Selulozik", location="İstanbul", weight="12 KG", choice="Tiner")
    selulozik5 = Paint.objects.filter(
        name="Selulozik", location="İstanbul", weight="5 KG", choice="Tiner")
    context = {
        "epoxy20": epoxy20,
        "epoxy12": epoxy12,
        "epoxy5": epoxy5,
        "polyurethane20": polyurethane20,
        "polyurethane12": polyurethane12,
        "polyurethane5": polyurethane5,
        "zehirli20": zehirli20,
        "zehirli12": zehirli12,
        "zehirli5": zehirli5,
        "sentetik20": sentetik20,
        "sentetik12": sentetik12,
        "sentetik5": sentetik5,
        "selulozik20": selulozik20,
        "selulozik12": selulozik12,
        "selulozik5": selulozik5,
    }
    return render(request, 'pages/tinerler-istanbul.html', context)


def big_paints_yalova(request):
    alkid = Paint.objects.filter(
        name="Alkid", location="Yalova", weight="20 KG", choice="Boya")
    ferropox = Paint.objects.filter(
        name="Ferropox", location="Yalova", weight="20 KG", choice="Boya")
    promega = Paint.objects.filter(
        name="Promega", location="Yalova", weight="20 KG", choice="Boya")
    ferromel = Paint.objects.filter(
        name="Ferromel", location="Yalova", weight="20 KG", choice="Boya")
    epoxy = Paint.objects.filter(
        name="Epoxy", location="Yalova", weight="20 KG", choice="Boya")
    akrilik = Paint.objects.filter(
        name="Akrilik", location="Yalova", weight="20 KG", choice="Boya")
    promarin = Paint.objects.filter(
        name="Promarin", location="Yalova", weight="20 KG", choice="Boya")
    underwater = Paint.objects.filter(
        name="Under Water", location="Yalova", weight="20 KG", choice="Boya")
    ferforje = Paint.objects.filter(
        name="Ferforje", location="Yalova", weight="20 KG", choice="Boya")
    antipas = Paint.objects.filter(
        name="Anti Pas", location="Yalova", weight="20 KG", choice="Boya")
    aluminyum = Paint.objects.filter(
        name="Aluminyum", location="Yalova", weight="20 KG", choice="Boya")
    resistant = Paint.objects.filter(
        name="Isıya Dayanıklı", location="Yalova", weight="20 KG", choice="Boya")
    context = {
        'alkid': alkid,
        'ferropox': ferropox,
        'promega': promega,
        'ferromel': ferromel,
        'epoxy': epoxy,
        'akrilik': akrilik,
        'promarin': promarin,
        'underwater': underwater,
        'ferforje': ferforje,
        'antipas': antipas,
        'aluminyum': aluminyum,
        'resistant': resistant,
    }
    return render(request, 'pages/buyuk-boyalar-yalova.html', context)


def small_paints_yalova(request):
    alkid = Paint.objects.filter(
        name="Alkid", location="Yalova", weight="5 KG", choice="Boya")
    ferropox = Paint.objects.filter(
        name="Ferropox", location="Yalova", weight="5 KG", choice="Boya")
    promega = Paint.objects.filter(
        name="Promega", location="Yalova", weight="5 KG", choice="Boya")
    ferromel = Paint.objects.filter(
        name="Ferromel", location="Yalova", weight="5 KG", choice="Boya")
    epoxy = Paint.objects.filter(
        name="Epoxy", location="Yalova", weight="5 KG", choice="Boya")
    akrilik = Paint.objects.filter(
        name="Akrilik", location="Yalova", weight="5 KG", choice="Boya")
    promarin = Paint.objects.filter(
        name="Promarin", location="Yalova", weight="5 KG", choice="Boya")
    underwater = Paint.objects.filter(
        name="Under Water", location="Yalova", weight="5 KG", choice="Boya")
    ferforje = Paint.objects.filter(
        name="Ferforje", location="Yalova", weight="5 KG", choice="Boya")
    antipas = Paint.objects.filter(
        name="Anti Pas", location="Yalova", weight="5 KG", choice="Boya")
    aluminyum = Paint.objects.filter(
        name="Aluminyum", location="Yalova", weight="5 KG", choice="Boya")
    resistant = Paint.objects.filter(
        name="Isıya Dayanıklı", location="Yalova", weight="5 KG", choice="Boya")
    context = {
        'alkid': alkid,
        'ferropox': ferropox,
        'promega': promega,
        'ferromel': ferromel,
        'epoxy': epoxy,
        'akrilik': akrilik,
        'promarin': promarin,
        'underwater': underwater,
        'ferforje': ferforje,
        'antipas': antipas,
        'aluminyum': aluminyum,
        'resistant': resistant,
    }
    return render(request, 'pages/kucuk-boyalar-yalova.html', context)


def thinners_yalova(request):
    epoxy20 = Paint.objects.filter(
        name="Epoxy", location="Yalova", weight="20 KG", choice="Tiner")
    epoxy12 = Paint.objects.filter(
        name="Epoxy", location="Yalova", weight="12 KG", choice="Tiner")
    epoxy5 = Paint.objects.filter(
        name="Epoxy", location="Yalova", weight="5 KG", choice="Tiner")
    polyurethane20 = Paint.objects.filter(
        name="Polyurethane", location="Yalova", weight="20 KG", choice="Tiner")
    polyurethane12 = Paint.objects.filter(
        name="Polyurethane", location="Yalova", weight="12 KG", choice="Tiner")
    polyurethane5 = Paint.objects.filter(
        name="Polyurethane", location="Yalova", weight="5 KG", choice="Tiner")
    zehirli20 = Paint.objects.filter(
        name="Zehirli", location="Yalova", weight="20 KG", choice="Tiner")
    zehirli12 = Paint.objects.filter(
        name="Zehirli", location="Yalova", weight="12 KG", choice="Tiner")
    zehirli5 = Paint.objects.filter(
        name="Zehirli", location="Yalova", weight="5 KG", choice="Tiner")
    sentetik20 = Paint.objects.filter(
        name="Sentetik", location="Yalova", weight="20 KG", choice="Tiner")
    sentetik12 = Paint.objects.filter(
        name="Sentetik", location="Yalova", weight="12 KG", choice="Tiner")
    sentetik5 = Paint.objects.filter(
        name="Sentetik", location="Yalova", weight="5 KG", choice="Tiner")
    selulozik20 = Paint.objects.filter(
        name="Selulozik", location="Yalova", weight="20 KG", choice="Tiner")
    selulozik12 = Paint.objects.filter(
        name="Selulozik", location="Yalova", weight="12 KG", choice="Tiner")
    selulozik5 = Paint.objects.filter(
        name="Selulozik", location="Yalova", weight="5 KG", choice="Tiner")
    context = {
        "epoxy20": epoxy20,
        "epoxy12": epoxy12,
        "epoxy5": epoxy5,
        "polyurethane20": polyurethane20,
        "polyurethane12": polyurethane12,
        "polyurethane5": polyurethane5,
        "zehirli20": zehirli20,
        "zehirli12": zehirli12,
        "zehirli5": zehirli5,
        "sentetik20": sentetik20,
        "sentetik12": sentetik12,
        "sentetik5": sentetik5,
        "selulozik20": selulozik20,
        "selulozik12": selulozik12,
        "selulozik5": selulozik5,
    }
    return render(request, 'pages/tinerler-yalova.html', context)


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
    else:
        return render(request, "pages/index.html", {"paint": paint})


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
