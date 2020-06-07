from django.conf.urls import re_path
from django.urls import path
from . import views

app_name = 'fdn_participant'
urlpatterns = [
    re_path(r'^$', views.register_participant, name='index'),
    # ex: /fdn/registration
    path('registration', views.register_participant, name='registration'),
]
