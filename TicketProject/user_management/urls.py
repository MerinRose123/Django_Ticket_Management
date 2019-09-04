from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    # path('register/', RegisterView.as_view(), name='register'),
    # path('', LoginView.as_view()),
    # path('logout/', views.logoutview, name='logoutview'),
    path('addticket/', views.addticket, name='addticket'),
    path('deleteticket/', views.deleteticket, name='deleteticket'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('', views.base, name='base'),
    path('register/', views.register, name='register'),
]