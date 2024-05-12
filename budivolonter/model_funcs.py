from django.db import transaction
#Kosta Novokmet
#vraca sve korisnike kao listu objekata
from . import models
def getUsers():
    return list(models.Korisnik.objects.all()) 

#Kosta Novokmet
#u bazu ubacuje novu aktivnost kao i sve propratne veze
def insertActivity(org,name,desc,spots,startD,endD,deadline,categories,country,city,reqs):
    with transaction.atomic():
        location = getLocation(country)
        activity = models.Aktivnost(idorg=org,naziv=name,opis=desc,brmesta=spots,datumod=startD,
                                    datumdo=endD,datumrok=deadline,mesto=city,lokacija=location)
        activity.save()
        for req_desc in reqs:
            req = models.Vestina(idakt=activity,opis=req_desc) 
            req.save()
        for cat in categories:
            cat_obj = getCategoryObject(cat)
            print(cat_obj.oblast,cat_obj.idobl)
            belongs = models.Pripada(idakt=activity,idobl=cat_obj)
            belongs.save()
#Kosta Novokmet
#vraca objekat Lokacija na osnovu drzave
def getLocation(country):
    result = models.Lokacija.objects.filter(drzava = country).first()
    if not result:
        from . import utils
        continent = utils.getContinent(country)
        location = models.Lokacija(drzava=country,kontinent=continent)
        location.save()
        return location
    return result
#Kosta Novokmet
#vraca listu imena svih kategorija
#potrebno za html ispis
def getCategoryNames():
    return list(models.Oblast.objects.all().values_list('oblast',flat=True))
    
#kosta Novokmet
#vraca objekat Oblasti na osnovu naziva Oblasti
#potrebno prilikom ubacivanja u bazu
def getCategoryObject(name):
    return models.Oblast.objects.filter(oblast=name).first()

