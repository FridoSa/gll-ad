from django.urls import path

from . import views

app_name = 'ad'
urlpatterns = [
    path(
        'mitarbeiter/',
        views.MitarbeiterListe.as_view(),
        name="mitarbeiterliste"
    ),
    path(
        'mitarbeiter/<int:pk>/',
        views.MitarbeiterDaten.as_view(),
        name="mitarbeiterdaten"
    ),
    path(
        'mitarbeiter/neu/',
        views.MitarbeiterNeu.as_view(),
        name="mitarbeiterneu"
    ),
]
