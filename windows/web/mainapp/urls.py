from django.urls import path
from .views import (index, resolve_ip, telegrambot, listip, get_ips, unresolve_ip, give_devices)

urlpatterns = [
    path("", name="index-page", view=index),
    path("telegram", name="telegrambot", view=telegrambot),
    path("ip", name="listip", view=listip),

    path("getdata/ip", name='ajax-ip', view=get_ips),

    path("post/resolve_ip", name='ajax-resolve-ip', view=resolve_ip),
    path("post/unresolve_ip", name='ajax-unresolve-ip', view=unresolve_ip),

    path("getdata/devices", view=give_devices)
]
