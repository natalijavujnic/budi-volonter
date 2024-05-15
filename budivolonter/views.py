from .utils import getCurrentUser
from django.shortcuts import redirect, render,HttpResponse
from django.http import HttpRequest,JsonResponse
from django.contrib.auth import login, logout
from . import models
from . import model_funcs
from datetime import datetime

#Kosta Novokmet
#renderuje welcome page
def welcome(request) -> HttpResponse:
    from . import utils
    context = {}
    context['navbar'] = utils.getNavbar(request)
    return render(request,'main_page.html',context) 

#Kosta Novokmet
#Poziva se prilikom poziva endpoint-a sa istim imenom. Treba da ubaci novu aktivnost u bazu
def open_activity(request:HttpRequest)-> HttpResponse:
    from . import utils
    if utils.getCurrentUser(request) is None:
        return redirect('login')
    elif utils.getCurrentUser(request).tip == 'V':
        return redirect('welcome') #todo redirect to error 404 page
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
                'cats': model_funcs.getCategoryNames(),
                'navbar' : utils.getNavbar(request)
                }
        return render(request,'open_activity.html',context)
    else:
        from . import utils
        context = {
                'countries':utils.getCountries,
                'status':'',
                'cats':model_funcs.getCategoryNames(),
                'navbar' : utils.getNavbar(request)
                }
        return render(request,'open_activity.html',context)

#Natalija Vujnic
#funcija za prikaz sopstvenog profila
def display_my_profile(request:HttpRequest)-> HttpResponse:
    ulogovan=request.user.is_authenticated
    if ulogovan:
        from . import utils
        korisnik=getCurrentUser(request)
        tipKorisnika=korisnik.tip
        print(tipKorisnika)
        if tipKorisnika=='O':
            context = {
                    'korisnik':korisnik,
                    'navbar':utils.getNavbar(request)
                    }
            return render(request, 'org_profile.html', context)
        elif tipKorisnika=='V':
            interesi=model_funcs.getInterests(korisnik.idkor)
            context = {
                    'korisnik':korisnik,
                    'navbar':utils.getNavbar(request),
                    'interesi': interesi
                    }
            return render(request, 'volonteer_profile.html', context)
        elif tipKorisnika=='A':
            stranica='admin_start.html'
            return render(request, stranica,{'navbar':utils.getNavbar(request)})
    return redirect('login')
#Anja Mihajlov
#Koristi se za insert nove organizacije u bazu
def reg_org(request: HttpRequest)-> HttpResponse:
    from . import utils
    if utils.getCurrentUser(request) is not None:
        return redirect('welcome')
    from . import utils
    context = {
            'navbar': utils.getNavbar(request)
            }
    if(request.method == 'POST'):
        parametri = request.POST
        ime = parametri['nazivOrganizacije']
        pib  = parametri['pib']
        telefon = parametri['telefon']
        email = parametri['email']
        lozinka = parametri['lozinka']

        if  model_funcs.UsrFromTel(tel=telefon,exists=True) or model_funcs.UsrFromPib(pib = pib,exists=True) or  model_funcs.UsrFromEmail(email=email,exists=True):
            poruka = "Već postoji korisnik sa datim telefonom, PIB-om ili e-mailom."

        else:
            poruka = "Organizacija je uspešno registrovana."
            model_funcs.insertOrganization(ime,pib,telefon,email,lozinka)
        context['poruka'] = poruka

        return render(request,'reg_org.html', context)

    return render(request, 'reg_org.html',context)


#Anja Mihajlov
#Registracija volontera
def reg_vol(request: HttpRequest)-> HttpResponse:
    if utils.getCurrentUser(request) is not None:
        return redirect('welcome')
    context = {
                'cats': model_funcs.getCategoryNames(),
                'navbar':utils.getNavbar(request)
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


        if model_funcs.UsrFromEmail(email=email,exists=True):
            context = {
                'poruka': "Već postoji korisnik sa datim e-mailom.",
                'cats': model_funcs.getCategoryNames()
                }
        elif godine<16 or godine>100:
            context = {
                'poruka': "Ne spadate u starosnu grupu za volontiranje",
                'cats': model_funcs.getCategoryNames(),
                'navbar':utils.getNavbar(request)
                }

        else:
            model_funcs.insertVolunteer(ime,prezime,datumRodj,email,lozinka,cats)
            context = {
                'poruka' :"Volonter je uspešno registrovan.",
                'cats': model_funcs.getCategoryNames(),
                'navbar':utils.getNavbar(request)
                }

        from . import utils
        return render(request,'reg_vol.html', context)

    return render(request, 'reg_vol.html', context)

#Djordje Sarovic
#funkcija za prikaz stranice za login
def login_page(request:HttpRequest)-> HttpResponse:
    from . import utils
    if utils.getCurrentUser(request) is not None:
        return redirect('welcome')
    if request.method == 'GET':
        return render(request, 'login.html',{'navbar': utils.getNavbar(request)})
    else:
        email = request.POST['email']
        password = request.POST['password']
        user = model_funcs.UsrFromEmail(email=email)
        if user:
            if user.check_password(password):
                login(request, user)
                return redirect('my_profile')
            else:
                return render(request, 'login.html', {'errorPassword':'Pogresna sifra','navbar': utils.getNavbar(request)})
        else:
            return render(request, 'login.html', {'errorEmail':'Pogresan email','navbar': utils.getNavbar(request)})
#Djordje Sarovic
def do_logout(request)-> HttpResponse:
    logout(request)
    return redirect('login')

#Djordje Sarovic
def activity_form(request:HttpRequest)-> HttpResponse:
    if getCurrentUser(request) is None:
        return redirect('login')
    elif getCurrentUser(request).tip == 'O':
        return redirect('welcome') #todo redirect to error 404 page
    from . import utils
    idAkt = request.GET.get('id', None)
    if idAkt is None:
        return redirect('welcome') #todo redirect to error 404 page
    aktivnost = model_funcs.getActivityById(idAkt)
    organizacija =model_funcs.getUsrById(aktivnost.idorg_id)
    context = {
        'naziv':aktivnost.naziv,
        'datumOd': aktivnost.datumod,
        'datumDo': aktivnost.datumdo,
        'organizacija_ime':organizacija.ime,
        'navbar': utils.getNavbar(request)
    }
    if request.method == 'GET':
        return render(request, 'activity_form.html', context)
    else:
        user = getCurrentUser(request)
        aktivnost = model_funcs.getActivityById(idAkt)
        if model_funcs.getApplicationsForActVol(idkor=user, idakt=aktivnost.idakt,exists=True):
            context['error'] = 'Vec ste se prijavili na ovu aktivnost'
            return render(request, 'activity_form.html', context)
        pismo = request.POST['pismo']
        if pismo == '':
            context['error'] = 'Morate uneti pismo'
            return render(request, 'activity_form.html', context)
        rezimeFile = request.FILES.get('rezime', None)
        model_funcs.insertApplication(idvol=user, idakt=idAkt, pismo=pismo, rezimeFile=rezimeFile)
        context['success'] = 'Uspesno ste se prijavili na aktivnost'
        return render(request, 'activity_form.html', context)

#Djordje Sarovic
def view_applications(request:HttpRequest):
    if getCurrentUser(request) is None:
        return redirect('login')
    elif getCurrentUser(request).tip == 'V':
        return redirect('welcome') #todo redirect to error 403 forbidden page
    from . import utils
    idAkt = request.GET.get('id', None)
    if idAkt is None:
        return redirect('welcome') #todo redirect to error 404 page
    aktivnost = model_funcs.getActivityById(idAkt)
    if aktivnost is None:
        return redirect('welcome') #todo redirect to error 404 page
    if aktivnost.idorg_id != getCurrentUser(request).idkor:
        return redirect('welcome') #todo redirect to error 403 forbidden page
    prijave = model_funcs.getApplicationsForAct(idakt=idAkt)
    context = {
        'naziv':aktivnost.naziv,
        'prijave': prijave,
        'navbar': utils.getNavbar(request)
    }
    return render(request, 'applications_view.html', context)
