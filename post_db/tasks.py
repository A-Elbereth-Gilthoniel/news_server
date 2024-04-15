from celery import shared_task
from . import models
from django.http import JsonResponse

@shared_task
def send_response():
    # d = {'id': 1, 'name': "ffff", 'author': "Rinat", 'rating': 0, 'date': 4}
    # #  {'id': 2, 'name': "afff 2", 'author': "fdf", 'rating': 0, 'date': 6},\
    # #  {'id': 3, 'name': "ffff 3", 'author': "fsfdf", 'rating': 0, 'date': 8},\
    # #  {'id': 4, 'name': "ffff 3", 'author': "fsfdf", 'rating': 0, 'date': 9},\
    # #  {'id': 5, 'name': "cfff 3", 'author': "fsfdf", 'rating': 0, 'date': 1},\
    # #  {'id': 6, 'name': "ffkf 3", 'author': "fsfdf", 'rating': 0, 'date': 3},\
    # #  {'id': 7, 'name': "ffff 3", 'author': "fsfdf", 'rating': 0, 'date': 2},\
    # #  {'id': 8, 'name': "dfff 3", 'author': "fsfdf", 'rating': 0, 'date': 11},\
    # #  {'id': 9, 'name': "ffgf 3", 'author': "fsfdf", 'rating': 0, 'date': 10},\
    # #  {'id': 10, 'name': "ffff 3", 'author': "fsfdf", 'rating': 0, 'date': 30}
    # return JsonResponse(d)
    marks = 10000
    a = marks / 0
    print(a)
