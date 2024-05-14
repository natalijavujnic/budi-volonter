#Kosta Novokmet
#uzima trenutnog korisnika koji je logovan na sistem
from django.http import HttpRequest

from budivolonter import models
from budivolonter.models import Korisnik


def getCurrentUser(request:HttpRequest):
    return models.Korisnik.objects.filter(email=request.user.get_username()).first()


#Kosta Novokmet
#vraca na kom kontinentu je neka drzava 
def getContinent(country):
    from .locations import countries,continents
    for contient,countries in continents.items():
        if country in countries: return contient
    return None


#vraca listu svih drzava na svetu
#za potrebe biranja drzava kada se pravi aktivnost
def getCountries():
    from .locations import countries
    return countries
