from django.urls import path
from . import tasks

urlpatterns = [
    path('', tasks.send_response),
]
