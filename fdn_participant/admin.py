from django.contrib import admin
from .models import EnvExposure, GeneMutation, Participant


admin.site.register(EnvExposure)
admin.site.register(GeneMutation)
admin.site.register(Participant)
