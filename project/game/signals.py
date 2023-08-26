from django.dispatch import receiver
from .models import Response
from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives


@receiver(post_save, sender=Response)
def response_created(instance,  created, **kwargs):
    if not created:
        return

    email = instance.post.author.email

    subject = f'Новый отклик'

    text_content = (
        f'{instance.post.author.username}, вам отклик от {instance.author} на объявление "{instance.get_absolute_url()}"!'
    )

    html_content = (
        f'{instance.post.author.username}, вам <a href="http://127.0.0.1:8000{instance.get_absolute_url()}">отклик</a> от {instance.author} на <a href="http://127.0.0.1:8000{instance.post.get_absolute_url()}">объявление</a>!'
    )

    msg = EmailMultiAlternatives(subject, text_content, None, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@receiver(post_save, sender=Response)
def response_accept(instance, **Kwargs):
    if not instance.status:
        return

    email = instance.author.email

    subject = f'Ваш отклик приняли!'

    text_content = (
        f'{instance.author.username}, ваш отклик к "{instance.post.title}" приняли!'
    )

    html_content = (
        f'{instance.author.username}, ваш <a href="http://127.0.0.1:8000{instance.get_absolute_url()}">отклик</a> к <a href="http://127.0.0.1:8000{instance.post.get_absolute_url()}">{instance.post.title}</a> приняли!'
    )

    msg = EmailMultiAlternatives(subject, text_content, None, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
