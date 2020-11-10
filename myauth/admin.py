from django.contrib import admin
from .models import Profile, State, Country

admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(State)