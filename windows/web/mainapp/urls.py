from django.urls import path
from .views import index, telegrambot, listip, get_ips

urlpatterns = [
    path("", name="index-page", view=index),
    path("telegram", name="telegrambot", view=telegrambot),
    path("ip", name="listip", view=listip),

    path("getdata/ip", name='ajax-ip', view=get_ips)

]
