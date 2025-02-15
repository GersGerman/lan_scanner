import json
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, "index.html")


def get_ips(request):
    import socket as sk

    sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

    sock.connect(("127.0.0.1", 6535))
    data = sock.recv(1024).decode()
    data = data[1:-1]
    data = data.split("}, ")
    Data = {"new": [], "old": []}
    for i in data:
        if i[-1] != "}":
            i + "}"
        print(i)
        Data["new"] + json.loads(i)
    print(data)
    print(Data)
    return JsonResponse(Data, content_type='application/json')


def telegrambot(request):
    return render(request, 'telegram.html')

def listip(request):
    return render(request, 'ip.html')