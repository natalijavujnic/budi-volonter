from . import model_funcs
from django.http import JsonResponse,HttpRequest
#kosta novokmet
#vraca sve aktivnosti kao listu recnika
def fetch_activities(request):
    from . import utils
    active_activities = model_funcs.getActiveActivities()
    archived_activities= model_funcs.getArchivedActivities()
    active_activities_list = utils.loadActivities(active_activities)
    archived_activities_list = utils.loadActivities(archived_activities)
    for act in archived_activities_list:
        reviews = model_funcs.getApplicationsForAct(act.get('id'))
        act['reviews'] = reviews
    print (reviews)
    return JsonResponse({'active_activities':active_activities_list,'archived_activities':archived_activities_list})
#kosta novokmet
#updatuje slobodna mesta aktivnosti
def update_free_spaces(request:HttpRequest):
    import json
    json_data = json.loads(request.body.decode('utf-8'))
    val = json_data['val']
    aktId = json_data['idakt']
    model_funcs.updateFreeSpaces(val,aktId)
    return JsonResponse({'message': 'Data received successfully'}, status=200)

