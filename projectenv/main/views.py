from django.shortcuts import render
from django.http import request
from .models import PaintList, Paint

# Create your views here.


def index(request):
    paints = Paint.objects.all()

    context = {
        'paints': paints
    }
    return render(request, 'pages/index.html', context)
