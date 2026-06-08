from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, TaskForm
from .models import Task


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'todo/register.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'todo/login.html'


class CustomLogoutView(LogoutView):
    pass


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
