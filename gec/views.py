from django.http import JsonResponse, HttpResponse
import requests

API_URL = 'http://nlp-thor.cs.nthu.edu.tw:1214/translate/'
HEADERS = {'Content-Type': 'application/json'}


def correct_it(request):
    if request.is_ajax() and request.method == 'POST':
        r = requests.post(API_URL, headers=HEADERS, data=request.body)
        # return JsonResponse(r.json())
        return HttpResponse(content=r.content, status=r.status_code)
