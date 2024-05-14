from .utils import getCurrentUser
from django.shortcuts import redirect, render,HttpResponse
from django.http import HttpRequest,JsonResponse
from django.contrib.auth import login, logout
from . import models
from . import model_funcs
from datetime import datetime

#Kosta Novokmet
#renderuje welcome page
def welcome(request):
   return render(request,'main_page.html') 

#Kosta Novokmet
#Poziva se prilikom poziva endpoint-a sa istim imenom. Treba da ubaci novu aktivnost u bazu
def open_activity(request:HttpRequest):
    if(request.method == 'POST'):
        parameters = request.POST
        cats = parameters.getlist('categories')
        reqs = parameters.get('reqs').strip().replace('\r','').split('\n')
        name = parameters['name'] 
        desc = parameters['desc']
        spots =  int(parameters['spots'])
        startDate = parameters['startDate']
        endDate = parameters['endDate']
        deadlineDate = parameters['deadlineDate']
        country = parameters['country']
        city = parameters['city']
        user = getCurrentUser(request)
        model_funcs.insertActivity(user,name,desc,spots,startDate,endDate,deadlineDate,cats,country,city,reqs)
        from . import utils
        context = {
                'countries':utils.getCountries,
                'status':'USPESNO DODATA AKTIVNOST!',
                'cats': model_funcs.getCategoryNames()
                }
        return render(request,'open_activity.html',context)
    else:
        from . import utils
        context = {
                'countries':utils.getCountries,
                'status':'',
                'cats':model_funcs.getCategoryNames()
                }
        return render(request,'open_activity.html',context)

#Natalija Vujnic
#funcija za prikaz sopstvenog profila
def display_my_profile(request:HttpRequest):
    ulogovan=request.user.is_authenticated
    if ulogovan:
        korisnik=getCurrentUser(request)
        tipKorisnika=korisnik.tip
        print(tipKorisnika)
        if tipKorisnika=='O':
            return render(request, 'org_profile.html', {'korisnik': korisnik})
        elif tipKorisnika=='V':
            interesi=model_funcs.getInterests(korisnik.idkor)
            return render(request, 'volonteer_profile.html', {'korisnik': korisnik, 'interesi': interesi})
        elif tipKorisnika=='A':
            stranica='admin_start.html'
            return render(request, stranica)
    return redirect('login')
#Anja Mihajlov
#Koristi se za insert nove organizacije u bazu
def reg_org(request: HttpRequest):
    if(request.method == 'POST'):
        parametri = request.POST
        ime = parametri['nazivOrganizacije']
        pib  = parametri['pib']
        telefon = parametri['telefon']
        email = parametri['email']
        lozinka = parametri['lozinka']

        if models.Korisnik.objects.filter(telefon =telefon).exists() or models.Korisnik.objects.filter(pib = pib).exists() or  models.Korisnik.objects.filter(email = email).exists() :
            poruka = "Već postoji korisnik sa datim telefonom, PIB-om ili e-mailom."

        else:
            poruka = "Organizacija je uspešno registrovana."
            model_funcs.insertOrganization(ime,pib,telefon,email,lozinka)

        from . import utils
        return render(request,'reg_org.html', {'poruka': poruka})

    return render(request, 'reg_org.html')


#Anja Mihajlov
#Registracija volontera
def reg_vol(request: HttpRequest):
    context = {
                'cats': model_funcs.getCategoryNames()
                }
    if(request.method == 'POST'):
        parametri = request.POST
        ime = parametri['ime']
        prezime = parametri['prezime']
        datumRodj = parametri['datumRodjenja']
        email = parametri['email']
        lozinka = parametri['lozinka']
        cats = parametri.getlist('categories')

        #provera za godine
        datum_rodjenja = datetime.strptime(datumRodj, "%Y-%m-%d")
        danas = datetime.now()
        godine = danas.year - datum_rodjenja.year - ((danas.month, danas.day) < (datum_rodjenja.month, datum_rodjenja.day))


        if models.Korisnik.objects.filter(email = email).exists() :
            context = {
                'poruka': "Već postoji korisnik sa datim e-mailom.",
                'cats': model_funcs.getCategoryNames()
                }
        elif godine<16 or godine>100:
            context = {
                'poruka': "Ne spadate u starosnu grupu za volontiranje",
                'cats': model_funcs.getCategoryNames()
                }

        else:
            model_funcs.insertVolunteer(ime,prezime,datumRodj,email,lozinka,cats)
            context = {
                'poruka' :"Volonter je uspešno registrovan.",
                'cats': model_funcs.getCategoryNames()
                }

        from . import utils
        return render(request,'reg_vol.html', context)

    return render(request, 'reg_vol.html', context)

#Djordje Sarovic
#funkcija za prikaz stranice za login
def login_page(request:HttpRequest):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST['email']
        password = request.POST['password']
        user = models.Korisnik.objects.filter(email=email).first()
        if user:
            if user.check_password(password):
                login(request, user)
                return redirect('my_profile')
            else:
                return render(request, 'login.html', {'errorPassword':'Pogresna sifra'})
        else:
            return render(request, 'login.html', {'errorEmail':'Pogresan email'})
#Djordje Sarovic
def do_logout(request):
    logout(request)
    return redirect('login')

#Djordje Sarovic
def activity_form(request:HttpRequest):
    idAkt = request.GET.get('id', None)
    if idAkt is None:
        return redirect('welcome') #todo redirect to error 404 page
    aktivnost = models.Aktivnost.objects.filter(idakt=idAkt).first()
    organizacija = models.Korisnik.objects.filter(idkor=aktivnost.idorg_id).first()
    if request.method == 'GET':
        return render(request, 'activity_form.html', {'naziv':aktivnost.naziv, 'datumOd': aktivnost.datumod, 'datumDo': aktivnost.datumdo, 'organizacija_ime':organizacija.ime})
    else:
        user = getCurrentUser(request)
        if models.Prijava.objects.filter(idvol=user, idakt=models.Aktivnost.objects.filter(idakt=request.GET.get('id')).first()).exists():
            return render(request, 'activity_form.html', {'naziv':aktivnost.naziv, 'datumOd': aktivnost.datumod, 'datumDo': aktivnost.datumdo, 'organizacija_ime':organizacija.ime, 'error':'Vec ste se prijavili na ovu aktivnost'})
        pismo = request.POST['pismo']
        if pismo == '':
            return render(request, 'activity_form.html', {'naziv':aktivnost.naziv, 'datumOd': aktivnost.datumod, 'datumDo': aktivnost.datumdo, 'organizacija_ime':organizacija.ime, 'error':'Morate uneti pismo'})
        rezime = request.POST['rezime']
        status = 'O'
        prijava = models.Prijava(idvol=user, idakt=models.Aktivnost.objects.filter(idakt=request.GET.get('id')).first(), pismo=pismo, rezime=rezime, status=status)
        prijava.save()
        return render(request, 'activity_form.html', {'naziv':aktivnost.naziv, 'datumOd': aktivnost.datumod, 'datumDo': aktivnost.datumdo, 'organizacija_ime':organizacija.ime, 'success':'Uspesno ste se prijavili na aktivnost'})