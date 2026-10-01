from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, "index.html")


def health(request):
    return JsonResponse(
        {
            "status": "online",
            "service": "Cloud Django Application",
            "timestamp": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        }
    )
