from django.conf.urls import re_path
from django.urls import path
from . import views

app_name = 'fdn_participant'
urlpatterns = [
    re_path(r'^$', views.home, name='index'),
    # ex: /fdn/home
    path('home', views.home, name='home'),
    # ex: /fdn/update_reviewed_status
    path('update_reviewed_status', views.update_reviewed_status, name='update_reviewed_status'),
    # ex: /fdn/registration
    path('registration', views.register_participant, name='registration'),
    # ex: /fdn/registration/add
    path('registration/add', views.add_participant, name='add'),
]
