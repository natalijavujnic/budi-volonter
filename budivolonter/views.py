from .utils import getCurrentUser
from django.shortcuts import render,HttpResponse
from django.http import HttpRequest
from . import models
from . import model_funcs

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
        user = getCurrentUser()
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
def display_my_profile(request):
    #ulogovan=request.user.is_authenticated
    ulogovan=1
    if ulogovan:
        korisnik=getCurrentUser()
        tipKorisnika=korisnik.tip
        print(tipKorisnika)
        if tipKorisnika=='o':
            stranica='org_profile.html'
            return render(request, 'org_profile.html', {'korisnik': korisnik})
        elif tipKorisnika=='v':
            stranica='vol_profile.html'
            interesi=model_funcs.getInterests(korisnik.idkor)
            return render(request, 'volonteer_profile.html', {'korisnik': korisnik, 'interesi': interesi})
        elif tipKorisnika=='a':
            stranica='admin_start.html'
    return render(request, 'login.html')

