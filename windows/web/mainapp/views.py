import json
import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

devices = {
    "new": [],
    "old": []
}


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
            i = i+ "}"
        
        i = i.replace("'", '"')
        if json.loads(i) in devices['old']:
            Data["old"].append(json.loads(i))
        else:
            Data["new"].append(json.loads(i))
            if json.loads(i) not in devices['new']:
                devices['new'].append(json.loads(i))
            


    return JsonResponse(Data, content_type='application/json')

def resolve_ip(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        for device in devices['new']:
            if data['ip'] == device['ip']:
                device = devices['new'].pop(devices['new'].index(device))
                devices['old'].append(device)


        return HttpResponse("OK")

    else:
        return HttpResponseBadRequest()
    
def unresolve_ip(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        for device in devices['old']:
            if data['ip'] == device['ip']:
                device = devices['old'].pop(devices['old'].index(device))
                devices['new'].append(device)

        return HttpResponse("OK")

    else:
            return HttpResponseBadRequest()

def give_devices(request):
    return HttpResponse(json.dumps(devices))

def telegrambot(request):
    return render(request, 'telegram.html')

def listip(request):
    return render(request, 'ip.html')

def create_tgbot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        open(f"{os.getcwd()}\\base_dir").write(data['token'])

        return HttpResponse("ok")

    else:
        return HttpResponseBadRequest()