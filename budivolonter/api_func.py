from . import model_funcs
from django.http import JsonResponse,HttpRequest
#kosta novokmet
#vraca sve aktivnosti organizacije 
#org = ona ciji se profil gleda
def fetch_activities_org(request:HttpRequest):
    from . import utils
    idkor = model_funcs.IdFromEmail(request.GET.get('email'))
    active_activities = model_funcs.getActiveActivitiesOrg(idkor)
    archived_activities= model_funcs.getArchivedActivitiesOrg(idkor)
    active_activities_list = utils.loadActivities(active_activities)
    archived_activities_list = utils.loadActivities(archived_activities)
    for act in archived_activities_list:
        reviews = model_funcs.getApplicationsForAct(act.get('id'))
        act['reviews'] = reviews
    print (reviews)
    return JsonResponse({'active_activities':active_activities_list,'archived_activities':archived_activities_list})


#kosta novokmet
#vraca sve aktivnosti na kojima je volonter 
#volonter = onaj ciji se profil gleda
def fetch_activities_vol(request):
    from . import utils
    idkor = model_funcs.IdFromEmail(request.GET.get('email'))
    activities = model_funcs.getActivitiesVol(idkor)
    activities_list = utils.loadActivities(activities)
    for act in activities_list:
        review = model_funcs.getApplicationsForActVol(act.get('id'),idkor)
        if review is None: act['review'] = 'null'
        else : act['review'] = review
    return JsonResponse({'archived_activities':activities_list})


#kosta novokmet
#updatuje slobodna mesta aktivnosti
def update_free_spaces(request:HttpRequest):
    import json
    json_data = json.loads(request.body.decode('utf-8'))
    val = json_data['val']
    aktId = json_data['idakt']
    model_funcs.updateFreeSpaces(val,aktId)
    return JsonResponse({'message': 'Data received successfully'}, status=200)

