from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random


@receiver(post_save, sender=User)
def response_created(instance,  created, **kwargs):
    if not created:
        return

    user = User.objects.get(username=instance.username)
    code = random.randint(100, 999)

    profile = Profile.objects.create(user=user, code_of_confirm=code)
    profile.save()

    send_mail(
        subject='Account email confirmation',
        message=f'Hi, your confirmation code: {code}',
        from_email=None,
        recipient_list=[instance.email],
    )