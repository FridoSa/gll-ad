from django.shortcuts import render
from django.views import generic

from django.urls import reverse

from .models import Mitarbeiter

class MitarbeiterListe(generic.ListView):
    model = Mitarbeiter
    

class MitarbeiterDaten(generic.edit.UpdateView):
    model = Mitarbeiter
    fields = '__all__'
    localized_fields = ['geboren', 'eintritt', 'austritt']
    
    def get_success_url(self):
        return reverse('ad:mitarbeiterdaten', args=[self.object.id])
    
    
class MitarbeiterNeu(generic.edit.CreateView):
    model = Mitarbeiter
    fields = '__all__'
    localized_fields = ['geboren', 'eintritt', 'austritt']
    
    def get_success_url(self):
        return reverse('ad:mitarbeiterliste')
