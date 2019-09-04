from django import forms
from .models import *
from django.contrib.auth.models import Group


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username',
                               widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class DeleteUserForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username',
                               widget=forms.TextInput(attrs={'placeholder': 'username'}))


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username',
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=50, label='first name',
                                 widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=50, label='first name',
                                widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.CharField(max_length=50, label='Email',
                            widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms. CharField(max_length=50, label='phone',
                             widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    DESIGNATION_CHOICES = [
        ('super_admin', 'super admin'),
        ('senior_system_admin', 'senior system admin'),
        ('system_admin', 'system admin'),
    ]
    designation = forms.CharField(label='Designation', widget=forms.Select(choices=DESIGNATION_CHOICES))


class TicketAddForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        labels = {
            "assigned_to": "Assigned to",
            "start_date": "start date",
            "end_date": "End date",
            "subject": "Subject",
            "message": "Message",
            "state": "state",
            "priority": "Priority"

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(groups__name='system_admin')


class TicketDeleteForm(forms.Form):
    ticket_id = forms.CharField(max_length=50, label='ticket id',
                                widget=forms.TextInput(attrs={'placeholder': 'Ticket Id'}))


# Form to edit the details of the current user
class EditForm(forms.ModelForm):
    username = forms.CharField(max_length=50, label='Username',
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=50, label='first name',
                                 widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=50, label='first name',
                                widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.CharField(max_length=50, label='Email',
                            widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(max_length=50, label='phone',
                            widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))

    DESIGNATION_CHOICES = [
        ('super_admin', 'super admin'),
        ('senior_system_admin', 'senior system admin'),
        ('system_admin', 'system admin'),
    ]
    designation = forms.CharField(label='Designation',
                                  widget=forms.Select(choices=DESIGNATION_CHOICES))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone')