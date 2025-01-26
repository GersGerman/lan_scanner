from django.urls import path
from .views import index, telegrambot, listip

urlpatterns = [
    path("", name="index-page", view=index),
    path("telegram", name="telegrambot", view=telegrambot),
    path("ip", name="listip", view=listip),
]
