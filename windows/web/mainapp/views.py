from django.shortcuts import render

def index(request):
    return render(request, "index.html")


def telegrambot(request):
    return render(request, 'telegram.html')

def listip(request):
    return render(request, 'ip.html')