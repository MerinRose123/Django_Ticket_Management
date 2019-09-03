from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', LoginView.as_view()),
    # path('logout/', views.logoutview, name='logoutview'),
]