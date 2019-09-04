from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    update_session_auth_hash,

)
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.views.generic.edit import FormView
from django.contrib.auth.models import Group
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url


# Adding user to group according to designation
def add_user_to_group(user, designation):
    # Adding the user to a group according to the designation option
    if designation == 'super_admin':
        group = Group.objects.get(name='super_admin')
    elif designation == 'senior_system_admin':
        group = Group.objects.get(name='senior_system_admin')
    else:
        group = Group.objects.get(name='system_admin')
    user.groups.add(group)


# Registering a new user
def register(request):
    if request.method == 'POST':  # processing the data after the data is posted
        form = RegisterForm(request.POST)
        username = form.data['username']
        email = form.data['email']
        password = form.data["password"]
        designation = form.data["designation"]
        if password == form.data["password1"]:  # checking if the the two passwords are same.
            # Checking if the username or password already exists in the database
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.error(request, 'Username or email already taken.')
                response = redirect('../register/')
            else:  # Creating a new user with given details
                q = User(first_name=form.data['first_name'], last_name=form.data['last_name'],
                         username=username, email=email, phone=form.data["phone"], password=make_password(password))
                q.save()
                add_user_to_group(q, designation)
                messages.success(request, 'user registered successfully.')
                response = redirect('../login/')
        else:
            messages.error(request, 'The passwords are not matching.')
            response = redirect('../register/')
        return response
    else:  # Rendering the form in html initially with get request
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


# To login a current user
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = form.data['username']
        password = form.data["password"]
        # Authenticating the user by checking in the database
        user = authenticate(username=username, password=password)
        '''
        if form.is_valid():
            if user is not None:
                login(request, user)
                messages.success(request, username + ' you are now logged in..!!!.')
                response = redirect('../home/')
                return response
        else:
            messages.error(request, 'Enter valid username and password.')
        '''
        if user is not None:
            login(request, user)
            messages.success(request, username + ' you are now logged in..!!!.')
            response = redirect('../home/')
            return response
        else:
            messages.error(request, 'username or password are not correct.')
            return render(request, 'login.html', {'form': form})

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def base(request):
    return render(request, 'base.html')


@login_required
def home(request):
    return render(request, 'base.html')


def addticket(request):
    # processing the data after the user has entered the details in the form
    if request.method == 'POST':
        form = TicketAddForm(request.POST)
        # Creating a new user with given details
        q = Ticket()
        q.save()
        # messages.success(request, 'user registered successfully.')
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
