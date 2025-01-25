from django.urls import path
from .views import index

urlpatterns = [
    path("", name="index-page", view=index)
]
