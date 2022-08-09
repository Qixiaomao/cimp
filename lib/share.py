from django.http import JsonResponse

def json_seq(data,**kwargs):
    JsonResponse(data,json_dumps_params={'ensure_ascii':False},**kwargs)