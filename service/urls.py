from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('howto/', views.HowToView.as_view(), name='howto'),
    path('about/', views.AboutView.as_view(), name='about'),
]