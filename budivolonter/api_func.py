from django.shortcuts import redirect
from budivolonter import models
from budivolonter.utils import getCurrentUser
from . import model_funcs
from django.http import HttpResponse, JsonResponse,HttpRequest
#kosta novokmet
#vraca sve aktivnosti organizacije 
#org = ona ciji se profil gleda
def fetch_activities_org(request:HttpRequest) -> JsonResponse:
    from . import utils
    idkor = model_funcs.IdFromEmail(request.GET.get('email'))
    active_activities = model_funcs.getActiveActivitiesOrg(idkor)
    archived_activities= model_funcs.getArchivedActivitiesOrg(idkor)
    active_activities_list = utils.loadActivities(active_activities)
    archived_activities_list = utils.loadActivities(archived_activities)
    for act in archived_activities_list:
        reviews = model_funcs.getApplicationsForAct(idakt=act.get('id'),finished=True,status='A')
        act['reviews'] = reviews
    print (reviews)
    return JsonResponse({'active_activities':active_activities_list,'archived_activities':archived_activities_list})


#kosta novokmet
#vraca sve aktivnosti na kojima je volonter 
#volonter = onaj ciji se profil gleda
def fetch_activities_vol(request) -> JsonResponse:
    from . import utils
    idkor = model_funcs.IdFromEmail(request.GET.get('email'))
    activities = model_funcs.getActivitiesVol(idkor)
    activities_list = utils.loadActivities(activities)
    for act in activities_list:
        review = model_funcs.getApplicationsForActVol(idakt=act.get('id'),idkor=idkor,finished=True)
        if review is None: act['review'] = 'null'
        else : act['review'] = review
    return JsonResponse({'activities':activities_list})


#kosta novokmet
#updatuje slobodna mesta aktivnosti
def update_free_spaces(request:HttpRequest) -> JsonResponse:
    import json
    json_data = json.loads(request.body.decode('utf-8'))
    val = json_data['val']
    aktId = json_data['idakt']
    model_funcs.updateFreeSpaces(val,aktId)
    return JsonResponse({'message': 'Data received successfully'}, status=200)

#Djordje Sarovic
#prihvata ili odbija prijavu
def resolveApplication(request:HttpRequest):
    if request.method != 'POST':
        return HttpResponse('Method not allowed', status=405)
    id = request.POST.get('id', None)
    status = request.POST.get('status', None)
    prijava = models.Prijava.objects.filter(idpri=id).first()
    prijava.status = status
    prijava.save()
    return HttpResponse('OK')


#Djordje Sarovic
#servira rezime prijave
def download(request:HttpRequest):
    if getCurrentUser(request) is None:
        return redirect('login')
    elif getCurrentUser(request).tip == 'V':
        return redirect('welcome') #todo redirect to error 403 forbidden page
    idPri = request.GET.get('id', None)
    if idPri is None:
        return redirect('welcome') #todo redirect to error 404 page
    prijava = models.Prijava.objects.filter(idpri=idPri).first()
    if prijava is None:
        return redirect('welcome') #todo redirect to error 404 page
    if prijava.idakt.idorg_id != getCurrentUser(request).idkor:
        return redirect('welcome') #todo redirect to error 403 forbidden page
    response = HttpResponse(prijava.rezime, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="rezime_'+prijava.idvol.ime+'_'+prijava.idvol.prezime+'_za_'+prijava.idakt.naziv+'.pdf"'
    return response
