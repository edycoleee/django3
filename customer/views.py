#customer/views.py
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from rest_framework.parsers import JSONParser

@csrf_exempt
def test1_customer(request):
    if request.method == 'GET':
        #data = JSONParser().parse(request)
        return JsonResponse({"response" : "Hello Django"})

@csrf_exempt
def test2_customer(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        return JsonResponse({"response" : data})