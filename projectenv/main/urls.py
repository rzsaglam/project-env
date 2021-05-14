from django.urls import path
from . import views

# http://127.0.0.1:8000/admin

urlpatterns = [
    path('', views.index, name='index'),
    path('ferropox', views.ferropox, name='ferropox'),
    path('alkid', views.alkid, name='alkid'),
    path('promega', views.promega, name='promega'),
]
