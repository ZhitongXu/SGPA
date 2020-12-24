from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Ques


@receiver(post_save, sender=User)
def create_ques(sender, instance, created, **kwargs):
    if created:
        Ques.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_ques(sender, instance, **kwargs):
    instance.ques.save()
