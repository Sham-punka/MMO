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

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user'] = User.objects.all()
    #     context['username'] = self.request.user.username
    #     context['email'] = self.request.user.email
    #     return context
    #
    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     return redirect('post_list')

    def post(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            # print(username)
            print(email)
        # if request.method == 'POST':
        #     username = request.POST['username']
        #     print(username)
        #     # password = request.POST['password']
        #     email = request.POST['email']
        #     print(email)
            # user = authenticate(request, username=username, password=password)
        print('я хотя бы существую')
        code = random.randint(100, 999)
        print(code)
        # user = User.objects.get(username=username)
        # print(user)
        # profile = Profile.objects.create(user=username, code_of_confirm=code)
        # profile.save()
        # us_id = list(Profile.objects.filter(code_of_confirm=code).values_list('user', flat=True))[:1]
        # us_id = int(*us_id)
        # print(us_id)
        # user = User.objects.get(id=us_id)
        # print(user)
        send_mail(
            subject='Account email confirmation',
            message=f'Hi, your confirmation code: {code}',
            from_email=None,
            recipient_list=[email],
        )

        return super().post(self, request, *args, **kwargs)

    # def form_valid(self, form):
    #     print(User.objects.all())
    #     username = form.cleaned_data.get("username")
    #     user = User.objects.get(username=username)
    #     user.is_active = False
    #     return super().form_valid(form)


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
    success_url = 'post_list'
    template_name = 'registration/confirm.html'

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.all()
        print(context['user'])
        context['username'] = User.objects
        print(context['username'])
        context['email'] = self.request.user
        print(context['email'])
        return context

    def form_valid(self, form):
        profile = list(Profile.objects.all().values_list('code_of_confirm', flat=True))
        code = str(form.cleaned_data['code_of_confirm'])

        if code in profile:
            self.request.user.is_active = True
            self.request.user.save()
            return super().form_valid(form)
        else:
            message = 'confirmation code is incorrect'
            return HttpResponse(message)