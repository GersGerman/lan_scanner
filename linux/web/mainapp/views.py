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
        if json.loads(i) in devices['old'] and json.loads(i) not in Data['old']:
            Data["old"].append(json.loads(i))
        else:

            if json.loads(i) not in devices['new'] and json.loads(i) not in Data['new']:
                devices['new'].append(json.loads(i))
                Data["new"].append(json.loads(i))
    
    for ip in devices['new']:
        while devices['new'].count(ip) > 1:
            devices['new'].remove(ip)
    
    for ip in devices['old']:
        while devices['old'].count(ip) > 1:
            devices['old'].remove(ip)
    
    return JsonResponse(devices, content_type='application/json')

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
    
    if devices['new'] == [] and devices['old'] == []:
        get_ips(request)
    return HttpResponse(json.dumps(devices))

def telegrambot(request):
    
    if open(f"{os.getcwd()}\\base_dir", 'r').read() != "":
        context = {"created": True}
    
    else:
        context = {"created": False}

    return render(request, 'telegram.html', context=context)

def listip(request):
    return render(request, 'ip.html')

def botstart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        open(f"{os.getcwd()}\\base_dir", 'r').write(data['token'])

        return HttpResponse("ok")

    else:
        return HttpResponseBadRequest()
    

def botstop(request):
    if request.method == 'POST':
        open(f"{os.getcwd()}\\base_dir", 'w').write("")


    else:
        return HttpResponseBadRequest()
