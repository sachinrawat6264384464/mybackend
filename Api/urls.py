from django.urls import path
from .views import receive_data

urlpatterns = [
    path("send-data/", receive_data),
]
