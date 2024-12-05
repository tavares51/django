from django.urls import path

from . import views

urlpatterns = [
    path("", views.CalculadoraView.as_view(), name='renda'),
]