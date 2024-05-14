from . import model_funcs
from django.http import JsonResponse,HttpRequest
#kosta novokmet
#vraca sve aktivnosti organizacije koja je logovana kao listu recnika
def fetch_activities_org(request):
    from . import utils
    logged_usr = utils.getCurrentUser(request)
    active_activities = model_funcs.getActiveActivitiesOrg(logged_usr.idkor)
    archived_activities= model_funcs.getArchivedActivitiesOrg(logged_usr.idkor)
    active_activities_list = utils.loadActivities(active_activities)
    archived_activities_list = utils.loadActivities(archived_activities)
    for act in archived_activities_list:
        reviews = model_funcs.getApplicationsForAct(act.get('id'))
        act['reviews'] = reviews
    print (reviews)
    return JsonResponse({'active_activities':active_activities_list,'archived_activities':archived_activities_list})


#kosta novokmet
#vraca sve aktivnosti na kojima je volonter koji je logovan ucestvovao
def fetch_activities_vol(request):
    from . import utils
    logged_usr = utils.getCurrentUser(request)
    activities = model_funcs.getActivitiesVol(logged_usr.idkor)
    activities_list = utils.loadActivities(activities)
    for act in activities_list:
        review = model_funcs.getApplicationsForActVol(act.get('id'),logged_usr.idkor)
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

