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


def addticket(request):
    # processing the data after the user has entered the details in the form
    if request.method == 'POST':
        form = TicketAddForm(request.POST)
        # Creating a new user with given details
        q = Ticket()
        q.save()
        #messages.success(request, 'user registered successfully.')
        response = redirect('../login/')
        return response

    else:
        # Rendering the form in html initially
        form = TicketAddForm()
    return render(request, 'addticket.html', {'form': form})


def deleteticket(request):
    if request.method == 'POST':
        form = TicketDeleteForm(request.POST)
        q = Ticket()
        q.save()
        response = redirect('../home/')
        return response

    else:
        # Rendering the form in html initially
        form = TicketDeleteForm()
    return render(request, 'deleteticket.html', {'form': form})


