from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('logout/', views.logoutview, name='logout_view'),
    path('addticket/', views.addticket, name='addticket'),
    path('deleteticket/', views.deleteticket, name='deleteticket'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('', views.base, name='base'),
    path('register/', views.register, name='register'),
    path('listticket/', views.listticket, name='listticket'),
    path('listuser/', views.listuser, name='listuser'),
    path('deleteuser/', views.deleteuser, name='deleteuser'),
    path('edituser/', views.edituser, name='edituser'),
    path('editticket/', views.editticket, name='editticket'),
    path('view_ticket_system_admin/', views.viewticket, name='viewticket'),
    path('edit_state_ticket/', views.edit_state_ticket, name='edit_state_ticket'),
]