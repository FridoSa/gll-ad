from django.urls import path

from . import views

urlpatterns = [
    path('mitarbeiter', views.employees.as_View, name="employees"),
]
