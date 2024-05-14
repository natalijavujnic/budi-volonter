from . import model_funcs
from django.http import JsonResponse
#kosta novokmet
#vraca sve aktivnosti kao listu recnika
def fetch_activities(request):
    from . import utils
    active_activities = model_funcs.getActiveActivities()
    archived_activities= model_funcs.getArchivedActivities()
    active_activities_list = utils.loadActivities(active_activities)
    archived_activities_list = utils.loadActivities(archived_activities)
    return JsonResponse({'active_activities':active_activities_list,'archived_activities':archived_activities_list})

