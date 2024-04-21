from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from registration.forms import RegistrationForm, UserLoginForm


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = UserLoginForm  # Ваша форма входа
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home_products_list')  # Редирект на домашнюю страницу после успешной авторизации


class RegisterView(FormView):
    template_name = 'registration/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')  # Редирект на страницу входа

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
