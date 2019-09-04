from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username',
                               widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


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
        widgets = {
            'ticket_id': forms.TextInput(attrs={'placeholder': 'Ticket id'}),
        }
        labels = {
            "ticket_id": "Ticket Id",
            "assigned_to": "Assigned to",
            "start_date": "start date",
            "end_date": "End date",
            "subject": "Subject",
            "message": "Message",
            "state": "state",
            "priority": "Priority"

        }

    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = User.objects.none()
    '''


class TicketDeleteForm(forms.Form):
    ticket_id = forms.CharField(max_length=50, label='ticket id',
                                widget=forms.TextInput(attrs={'placeholder': 'Ticket Id'}))