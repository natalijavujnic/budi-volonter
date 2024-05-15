from django.db import transaction
#Kosta Novokmet
#vraca sve korisnike kao listu objekata
from . import models
def getUsers():
    return list(models.Korisnik.objects.all()) 

#Kosta Novokmet
#u bazu ubacuje novu aktivnost kao i sve propratne veze
def insertActivity(org,name,desc,spots,startD,endD,deadline,categories,country,city,reqs) -> None:
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
def getLocation(country) -> models.Lokacija:
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
def getCategoryNames() -> list:
    return list(models.Oblast.objects.all().values_list('oblast',flat=True))
    
#kosta Novokmet
#vraca objekat Oblasti na osnovu naziva Oblasti
#potrebno prilikom ubacivanja u bazu
def getCategoryObject(name) -> models.Oblast:
    return models.Oblast.objects.filter(oblast=name).first()


#Natalija Vujnic
#funkcija vraca interesovanja korisnika
def getInterests(id) -> list:
    return models.ZanimaGa.objects.filter(idkor_id=id).values_list('idobl__oblast', flat=True)
    
#Anja Mihajlov
#U bazu unosi novog korisnika koji je tipa O, tj. organizacija
def insertOrganization(ime,pib,telefon,email,lozinka) -> None:
    with transaction.atomic():
        organizacija = models.Korisnik(ime = ime, password = lozinka, email = email, pib = pib, telefon = telefon, tip = 'O')
        organizacija.set_password(lozinka)
        organizacija.save()
       
#Anja Mihajlov
#U bazu unosi novog korisnika tipa V, tj. volontera, radi insert u zanimaga
def insertVolunteer(ime,prezime,datumRodj,email,lozinka,cats) -> None:
    with transaction.atomic():
        volonter = models.Korisnik (ime = ime, prezime = prezime, datumrodj = datumRodj, password = lozinka, email = email, tip ='V')
        volonter.set_password(lozinka)
        volonter.save()
        for cat in cats:
            unos = models.ZanimaGa(idkor = volonter, idobl = getCategoryObject(cat))
            unos.save()

#Kosta Novokmet
#vraca sve aktivnosti kao listu
def getAllActivities() -> list[models.Aktivnost]:

    return list(models.Aktivnost.objects.all())

#Kosta Novokmet
#vraca sve prijave kao listu
def getAllApplications() -> list[models.Aktivnost]:

    return list(models.Prijava.objects.all())
#Kosta Novokmet 
#vraca sve aktivnosti iz baze koje se nisu zavrsile za odredjenu organizaciju
def getActiveActivitiesOrg(korID) -> list:
    acts = getAllActivities()
    from . import utils

    return [act for act in acts if not utils.datePassed(act.datumdo) and act.idorg.idkor == korID]

#Kosta Novokmet 
#vraca sve aktivnosti iz baze koje su se zavrsile za odredjenu organizaciju
def getArchivedActivitiesOrg(korID) -> list:
    acts = getAllActivities()
    from . import utils
    return [act for act in acts if utils.datePassed(act.datumdo) and act.idorg.idkor == korID]


#Kosta Novokmet 
#vraca sve aktivnosti na kojima je volonter ucestvovao
def getActivitiesVol(korID) -> list:
    acts = getAllApplications()
    from . import utils
    return [act.idakt for act in acts if utils.datePassed(act.idakt.datumdo) and act.idvol.idkor == korID]




#Kosta Novokmet
#vraca sve zahteve aktivnosti
def getActivityReqs(actID) -> list:
    return  list(models.Vestina.objects.filter(idakt=actID).all().values_list('opis',flat=True))

#Kosta Novokmet
#vraca sve prijave za odredjenu aktivnost u vidu liste recnika
# opciono se prosledi status prijava koje hocemo i da li je ta aktivnost prosla
#finished=True ako jeste i status='O/R/A'
#mora se proslediti idact=..
def getApplicationsForAct(**kwargs) -> list[dict]:
    app_status = kwargs.get('status','O')
    passed = kwargs.get('finished',False)
    actID = kwargs['idakt']
    apps = list(models.Prijava.objects.filter(idakt=actID,status=app_status).all())
    from . import utils
    if(passed == True ):
        return [
                {
                    'preporukavol' :app.preporukavol,
                    'preporukaorg' :app.preporukaorg,
                    'komvol'       : app.komvol,
                    'komorg'       : app.komorg,
                    'status'       : app.status,
                    'idpri'        : app.idpri,
                    'idakt'        : app.idakt.idakt,
                    'idvol'        : app.idvol.idkor,
                    'volname'      : app.idvol.ime,
                    'vollastname'  : app.idvol.prezime,
                    'pismo'        : app.pismo,
                    'rezime'       : app.rezime
                    }
                for app in apps if utils.datePassed(app.idakt.datumdo)
                ]

    else:
        return [
                {
                    'preporukavol' :app.preporukavol,
                    'preporukaorg' :app.preporukaorg,
                    'komvol'       : app.komvol,
                    'komorg'       : app.komorg,
                    'status'       : app.status,
                    'idpri'        : app.idpri,
                    'idakt'        : app.idakt.idakt,
                    'idvol'        : app.idvol.idkor,
                    'volname'      : app.idvol.ime,
                    'vollastname'  : app.idvol.prezime,
                    'pismo'        : app.pismo,
                    'rezime'       : app.rezime
                    }
                for app in apps
                ]

#Kosta Novokmet
#vraca prijavu odredjenog volontera za odredjenu aktivnost kao recnik, ako nema vraca None
#opciono finished=True ako hocemo prijavu samo ako je ta akt prosla
#idakt i idkor moraju da se stave kao key val pair u pozivu fje
def getApplicationsForActVol(**kwargs) -> dict:
    passed = kwargs.get('finished',False)
    actID = kwargs['idakt']
    korID = kwargs['idkor']
    exists = kwargs.get('exists',False)
    if exists == True :return models.Prijava.objects.filter(idakt=actID, idvol=korID).exists()
    if passed == True:
        from . import utils
        if app and utils.datePassed(app.idakt.datumdo):
            return {
                    'preporukavol': app.preporukavol,
                    'preporukaorg': app.preporukaorg,
                    'komvol': app.komvol,
                    'komorg': app.komorg,
                    'status': app.status,
                    'idpri': app.idpri,
                    'idakt': app.idakt.idakt,
                    'idvol': app.idvol.idkor,
                    'volname': app.idvol.ime,
                    'vollastname': app.idvol.prezime,
                    'pismo':app.pismo,
                    'rezime' : app.rezime
                    }

        else: return None
    else:
        if app:
            return {
                    'preporukavol': app.preporukavol,
                    'preporukaorg': app.preporukaorg,
                    'komvol': app.komvol,
                    'komorg': app.komorg,
                    'status': app.status,
                    'idpri': app.idpri,
                    'idakt': app.idakt.idakt,
                    'idvol': app.idvol.idkor,
                    'volname': app.idvol.ime,
                    'vollastname': app.idvol.prezime,
                    'pismo': app.pismo,
                    'rezime': app.rezime
                    }
        else: return None

            

#Kosta Novokmet
#updatuje u bazi broj slob mesta za akktivnost actID na new_val
def updateFreeSpaces(new_val,actID) -> None:
    print(f'called with val{new_val} id{actID}')
    act = models.Aktivnost.objects.get(idakt = actID);
    act.brmesta = new_val
    act.save()


#Kosta Novokmet
#vraca user id ili user obj na osnovu email-a
def UsrFromEmail(**kwargs):
    target_email = kwargs['email']
    id = kwargs.get('id',False)
    exists = kwargs.get('exists',False)
    if exists == True :return models.Korisnik.objects.filter(email=target_email).exists()
    usr = models.Korisnik.objects.filter(email=target_email).first()
    if id: return usr.idkor
    else: return usr
#Kosta Novokmet
#vraca usera na osnovu pib-a
def UsrFromPib(**kwargs):
    target_pib = kwargs['pib']
    exists = kwargs.get('exists',False)
    if exists == True: return models.Korisnik.objects.filter(pib=target_pib).exists()
    usr = models.Korisnik.objects.filter(pib=target_pib).first()
    return usr

#Kosta Novokmet
#vraca usera na osnovu pib-a
def UsrFromTel(**kwargs):
    target_tel = kwargs['tel']
    exists = kwargs.get('exists',False)
    if exists == True: return models.Korisnik.objects.filter(telefon=target_tel).exists()
    usr = models.Korisnik.objects.filter(telefon=target_tel).first()
    return usr

def getApplicationById(idPri) -> models.Prijava:
    return models.Prijava.objects.filter(idpri=idPri).first()

#Kosta Novokmet
def getActivityById(idAkt) -> models.Aktivnost:
    return models.Aktivnost.objects.filter(idakt=idAkt).first()


#Kosta Novokmet
def getUsrById(id) -> models.Korisnik:
    return models.Korisnik.objects.filter(idkor=id).first()


def insertApplication(idvol, idakt, pismo, rezimeFile) -> None:
    with transaction.atomic():
        prijava = models.Prijava(idvol=idvol, idakt= getActivityById(idAkt=idakt), pismo=pismo, rezime=rezimeFile.file.read() if rezimeFile is not None else None, status='O')
        prijava.save()
