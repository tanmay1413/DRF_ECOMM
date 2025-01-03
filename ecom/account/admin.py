from django.contrib import admin
from .models import *


class Account(admin.ModelAdmin):
  list_display = ['phone_number', 'password', 'first_name','last_name', 'email','is_staff']
  search_fields = ['phone_number', 'email']
  list_filter = ['is_staff']
  

admin.site.register(CustomUser, Account)