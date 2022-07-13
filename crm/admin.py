from django.contrib import admin

from crm.models import Client, ClientWallet

# Register your models here.
admin.site.register(Client)
admin.site.register(ClientWallet)