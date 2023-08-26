from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
import os
from .forms import PostForm, ResponseForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from datetime import datetime
from .filters import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'postlist.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class ResponseList(LoginRequiredMixin, ListView):
    raise_exception = True
    model = Response
    ordering = '-dateCreation'
    template_name = 'responses.html'
    context_object_name = 'responses'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ResponseFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        myresp = Response.objects.filter(author=self.request.user)
        context['myresp'] = myresp
        return context


class ResponseCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = ResponseForm
    model = Response
    template_name = 'response_create.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        response = form.save(commit=False)
        response.post = Post.objects.get(pk=self.request.resolver_match.kwargs['pk'])
        response.author = self.request.user
        return super().form_valid(form)


class ResponseDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Response
    template_name = 'response_delete.html'
    success_url = reverse_lazy('resp_list')


class ResponseDetail(LoginRequiredMixin, DetailView):
    model = Response
    template_name = 'response.html'
    context_object_name = 'response'


@login_required
def response_accept(request, pk):
    resp = Response.objects.get(id=pk)
    print(resp.status)
    resp.status = True
    resp.save()
    print(resp.status)
    return render(request, 'accept.html')


@login_required
def response_reject(request, pk):
    resp = Response.objects.get(id=pk)
    resp.status = False
    resp.save()
    return render(request, 'reject.html')