from django.views.generic import CreateView, FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth.models import User
#from .utils import *
from .forms import RegisterUserForm, LoginUserForm,  CodeForm
from django.http import HttpResponse
from django.contrib.auth import logout, login
from django.shortcuts import redirect
import random
from .models import Profile


class RegisterUser(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('confirm')

    def form_valid(self, form):
        my_user = form.save(commit=False)
        my_user.is_active = False

        return super().form_valid(form)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.all()
        return context


def logout_user(request):
    logout(request)
    return redirect('post_list')


class ConfirmUser(FormView):
    model = Profile
    form_class = CodeForm
    success_url = '/announcement'
    template_name = 'registration/confirm.html'

    def form_valid(self, form):

        user = User.objects.get(id=list(Profile.objects.all().values_list('user_id', flat=True))[-1])
        user.is_active = False
        profile = list(Profile.objects.all().values_list('code_of_confirm', flat=True))
        code = str(form.cleaned_data['code_of_confirm'])

        if code in profile:
            user.is_active = True
            user.save()
            return super().form_valid(form)
        else:
            message = 'confirmation code is incorrect'
            return HttpResponse(message)
