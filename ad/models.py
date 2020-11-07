from django.db import models

class Mitarbeiter(models.Model):
    GENDER_CHOICES = [
        ('f', 'Frau'),
        ('m', 'Herr'),
        ('d', '*'),
    ]
    KINDS_OF_DEPLOYMENT = [
        ('h', 'Helfer*in'),
        ('a', 'Angestellt'),
        ('f', 'FSJ'),
    ]
    anrede = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='d',
    )
    vorname = models.CharField(max_length=20)
    nachname = models.CharField(max_length=30)
    nr = models.CharField(
        max_length=5,
        blank=True,
        help_text='Bei gleichen Vor- und Nachnamen'
    )
    adresszusatz = models.CharField(max_length=20, blank=True)
    strasse = models.CharField(max_length=50)
    pLZ = models.CharField(max_length=5)
    ort = models.CharField(max_length=20)
    telefon = models.CharField(max_length=20, blank=True)
    handy = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    geboren = models.DateField()
    eintritt = models.DateField()
    austritt = models.DateField(blank=True, null=True)
    iBAN = models.CharField(max_length=34)
    bankname = models.CharField(max_length=30)
    art = models.CharField(
        max_length=1,
        choices=KINDS_OF_DEPLOYMENT,
        default='h',
    )
    personenkonto = models.CharField(max_length=20, blank=True)
    stundenlohn = models.CharField(max_length=10, blank=True)
    limit = models.CharField(
        'Jahreslimit für Aufwandsentschädigung',
        max_length=5,
        blank=True
    )
    gesperrt = models.BooleanField(
        'Verdienstabrechnung gesperrt',
        default=False
    )
    meldung = models.TextField('Meldung bei Verdienstabrechnung', blank=True)
    notizen = models.TextField('AD-Notizen', blank=True)
    
