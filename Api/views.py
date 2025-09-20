from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def receive_data(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        age = data.get("age")
        return JsonResponse({"message": f"Hello {name}, age {age} received!"})
