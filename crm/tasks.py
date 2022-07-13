from __future__ import absolute_import, unicode_literals
import requests, json
from .models import Client
from celery import shared_task

@shared_task
def create_client():
    end_point = 'https://62c2c06cff594c656764970a.mockapi.io/users'
    user = requests.get(end_point)
    json_data = json.loads(user.text)

    for i in json_data['data']:
        Client.objects.create(cid = i['cid'],
            first_name = i['first_name'],
            last_name = i['last_name'],
            country_code = i['country_code'],
            email = i['email'],
            address = i['address'],
            phone = i['phone']
        )