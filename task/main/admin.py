from django.contrib import admin
from .models import CustomUser, CustomGroup

admin.site.register(CustomUser)
admin.site.register(CustomGroup)
