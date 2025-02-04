from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, "index.html")


def get_ips(request):

    return JsonResponse({"trused": {
                            "127.0.0.1": 'Galaxy A51',
                            "127.0.0.2": 'Galaxy A52',},
                        "new":{
                            "127.0.0.3": 'Galaxy A53',
                            "127.0.0.4": 'Galaxy A54',
                            "127.0.0.5": 'Galaxy A55',
            }
        })


def telegrambot(request):
    return render(request, 'telegram.html')

def listip(request):
    return render(request, 'ip.html')