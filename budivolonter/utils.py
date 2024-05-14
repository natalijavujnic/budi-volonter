from django.http import HttpRequest
from budivolonter import models
from budivolonter.models import Korisnik

#Djordje Sarovic
def getCurrentUser(request:HttpRequest):
    return models.Korisnik.objects.filter(email=request.user.get_username()).first()


#Kosta Novokmet
#vraca na kom kontinentu je neka drzava 
def getContinent(country):
    from .locations import countries,continents
    for contient,countries in continents.items():
        if country in countries: return contient
    return None


#Kosta Novokmet
#vraca listu svih drzava na svetu
#za potrebe biranja drzava kada se pravi aktivnost
def getCountries():
    from .locations import countries
    return countries


#Kosta Novokmet
#proverava da li je datum prosao 
#ako je datum prosao, vraca true 
from datetime import date 
def datePassed(date:date):
   curr_date = date.today();
   if (curr_date > date): return True
   return False



#Kosta Novokmet
#pravi listu aktivnosti, svaka aktivnost je recnik
def loadActivities(acts):
    from . import model_funcs
    act_list= []
    for act in acts:
        act_data = {}
        oblasti = list(act.oblasti.all().values_list(flat=True))
        zahtevi = model_funcs.getActivityReqs(act.idakt)
        act_data['naziv'] = act.naziv
        act_data['opis'] = act.opis
        act_data['oblasti'] = oblasti
        act_data['zahtevi'] = zahtevi
        act_data['brmesta'] = act.brmesta
        act_data['datumStart'] = act.datumod
        act_data['datumEnd'] = act.datumdo
        act_data['datumRok'] = act.datumrok
        act_data['drzava'] = act.lokacija.drzava
        act_data['kontinent'] = act.lokacija.kontinent
        act_data['org'] = act.idorg.ime
        act_list.append(act_data)
    return act_list 
