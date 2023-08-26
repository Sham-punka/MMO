from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class CodeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'code_of_confirm'
        ]

    # def save(self, request):
    #     user = super().save(request)
    #     common_users = Group.objects.get(name="common users")
    #     user.groups.add(common_users)
    #
    #     subject = 'Добро пожаловать на нашу доску объявлений!'
    #     text = f'{user.username}, вы успешно зарегистрировались на сайте!'
    #     html = (
    #         f'<b>{user.username}</b>, вы успешно зарегистрировались на '
    #         f'<a href="http://127.0.0.1:8000/announcement">сайте</a>!'
    #     )
    #     msg = EmailMultiAlternatives(
    #         subject=subject, body=text, from_email=None, to=[user.email]
    #     )
    #     msg.attach_alternative(html, "text/html")
    #     msg.send()
