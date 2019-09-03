from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    update_session_auth_hash,

)
from django.http import HttpResponse
from django.views.generic.edit import FormView
from .forms import *


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/home/'

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/home/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
