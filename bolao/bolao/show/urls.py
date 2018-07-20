from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'login', auth_views.login, {'template_name': 'show/login.html'}, name='login'),
    path(r'logout', auth_views.logout, {'template_name': 'show/index.html'}, name='logout'),
    path('convite', views.convidarAmigo, name='convite')
]