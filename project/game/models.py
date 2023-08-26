from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    dateCreation = models.DateField(auto_now_add=True)
    text = models.TextField()
    CATEGORY_CHOICES = (
        ('tank', 'Танк'),
        ('heal', 'Хил'),
        ('dd', 'ДД'),
        ('trader', 'Торговец'),
        ('gild', 'Гилдмастер'),
        ('quest', 'Квестгивер'),
        ('blacksmith', 'Кузнец'),
        ('leatherworker', 'Кожевник'),
        ('potion', 'Зельевар'),
        ('spell', 'Мастер заклинаний'),
    )
    category = models.CharField(max_length=13,choices=CATEGORY_CHOICES, default='tank')
    image = models.FileField(upload_to="game/", null=True, default=None, blank=True)
    video = models.FileField(upload_to="game/", null=True, default=None, blank=True)
    document = models.FileField(upload_to="game/", null=True, default=None, blank=True)

    def __str__(self):
        return f'{self.title}: {self.text}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    dateCreation = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('response', args=[str(self.id)])
