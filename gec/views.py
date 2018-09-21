from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests

API_URL = 'http://thor.nlplab.cc:1214/translate/'
HEADERS = {'Content-Type': 'application/json'}


# @csrf_exempt
def correct_it(request):
    if request.is_ajax() and request.method == 'POST':
        r = requests.post(API_URL, headers=HEADERS, data=request.body)
        # return JsonResponse(r.json())
        return HttpResponse(content=r.content, status=r.status_code)
