from django.contrib.auth.views import logout_then_login, logout, login
from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='home.html'
    ), name='index'),
    path('index/', TemplateView.as_view(
        template_name='home.html'
    ), name='index'),

    path('register/', views.RegisterView.as_view(), name='register'),
    path('activate/<str:token>/', views.ActivateView.as_view(), name='activate'),
    path('login/',login, {'template_name': 'registration/login.html'}, name='login'),
    path('logout/', logout,{'template_name': 'registration/logged_out.html'}, name='logout'),

]

