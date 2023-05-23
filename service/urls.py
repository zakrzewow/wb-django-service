from django.shortcuts import redirect
from django.urls import path

from . import views

urlpatterns = [
    path('', lambda r: redirect('index', chromosome='chr1'), name='default_redirect'),
    path('chromosome/<str:chromosome>/', views.IndexView.as_view(), name="index"),
    path('howto/', views.how_to_view, name='howto'),
    path('about/', views.about_view, name='about'),
]