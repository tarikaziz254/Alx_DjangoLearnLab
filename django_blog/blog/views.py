from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.urls import reverse_lazy

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')


class ProfileUpdateView(UpdateView):
    model = User
    template = 'registration/profile.html'
    fields = ['username', 'email']
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


LoginView = auth_views.LoginView.as_view(template_name = 'registration/login.html')
LogoutView = auth_views.LogoutView.as_view(next_page = 'login')