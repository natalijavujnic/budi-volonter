from django.http import HttpRequest
from budivolonter import models
from budivolonter.models import Korisnik

#Djordje Sarovic
def getCurrentUser(request:HttpRequest) -> Korisnik|None:
    if request.user.is_anonymous:
        return None
    return models.Korisnik.objects.filter(email=request.user.get_username()).first()



#Kosta Novokmet
#vraca na kom kontinentu je neka drzava 
def getContinent(country) -> dict:
    from .locations import countries,continents
    for contient,countries in continents.items():
        if country in countries: return contient
    return None


#Kosta Novokmet
#vraca listu svih drzava na svetu
#za potrebe biranja drzava kada se pravi aktivnost
def getCountries() -> tuple:
    from .locations import countries
    return countries


#Kosta Novokmet
#proverava da li je datum prosao 
#ako je datum prosao, vraca true 
from datetime import date 
def datePassed(date:date) -> bool:
    curr_date = date.today()
    if (curr_date > date): 
       return True
    return False



#Kosta Novokmet
#pravi listu aktivnosti, svaka aktivnost je recnik
def loadActivities(acts) -> list:
    from . import model_funcs
    act_list= []
    for act in acts:
        act_data = {}
        oblasti = list(act.oblasti.all().values_list(flat=True))
        zahtevi = model_funcs.getActivityReqs(act.idakt)
        act_data['id'] = act.idakt
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


#Kosta Novokmet
def getNavbar(request) -> str:
    usr = getCurrentUser(request)
    if usr is None:
        user_type= 'UNR'
    else:
        user_type = usr.tip
    if(user_type == 'O'):
        with open('./budivolonter/html/navbar_org.html','r') as file:
            return file.read()
    elif (user_type == 'V'):
        with open('./budivolonter/html/navbar_vol.html','r') as file:
            return file.read()
    elif (user_type == 'A'):
        with open('./budivolonter/html/navbar_admin.html','r') as file:
            return file.read()
    elif(user_type == 'UNR'):
        with open('./budivolonter/html/navbar_unreg.html','r') as file:
            return file.read()
