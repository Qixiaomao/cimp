from django.http import JsonResponse

def json_seq(data,**kwargs):
    return JsonResponse(data,json_dumps_params={'ensure_ascii':False},**kwargs)