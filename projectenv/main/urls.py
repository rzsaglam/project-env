from re import template
from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

# http://127.0.0.1:8000/admin

urlpatterns = [
    path('', views.index, name='index'),
    path('ferropox', views.ferropox, name='ferropox'),
    path('alkid', views.alkid, name='alkid'),
    path('promega', views.promega, name='promega'),
    path('buyuk-boyalar-yalova', views.big_paints_yalova,
         name='buyuk-boyalar-yalova'),
    path('promega-yalova', views.promega_yalova, name='promega_yalova'),
    path('kucuk-boyalar-yalova', views.small_paints_yalova,
         name='kucuk-boyalar-yalova'),
    path('edit/<int:id>', views.editPaint),
    path('update/<int:id>', views.updatePaint),
    path('boya-ekle', views.addPaint, name="boya_ekle"),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name="loginView"),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'),
         name='logoutView'),
    path('accounts/profile/', views.profile, name='profile'),
]
