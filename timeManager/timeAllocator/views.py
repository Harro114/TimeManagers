from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.views.generic import FormView

from timeAllocator.forms import RegisterForm, LoginForm
from timeAllocator.models import User


class RegistrationView(FormView):
    form_class = RegisterForm
    template_name = "timeAllocator/registration.html"
    success_url = "/"

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            form.add_error('username', "Пользователь с таким именем уже существует.")
            return self.form_invalid(form)
        User.create_user(form.cleaned_data["username"], form.cleaned_data["email"], form.cleaned_data["password"])
        return super(RegistrationView, self).form_valid(form)



class LoginView(FormView):
    form_class = LoginForm
    template_name = "timeAllocator/login.html"
    success_url = "/"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            #
            form.add_error("username", 'Неверный никнейм или пароль')
            return super().form_invalid(form)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect(request, 'timeAllocator/index.html')


def task_list(requests):
    return render(requests, "timeAllocator/index.html")
