from django.db.models.signals import post_save
from .models import Client, ClientWallet
from django.dispatch import receiver

@receiver(post_save, sender=Client)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        ClientWallet.objects.create(clients=instance)

@receiver(post_save, sender = Client)
def create_wallet(sender, instance, **kwargs):
    instance.clientwallet.save()