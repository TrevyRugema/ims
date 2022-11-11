from django.contrib import admin
from .models import User
from django.contrib.auth import get_user_model
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_employee', 'is_finance','is_general_manager','is_logistic']

user=get_user_model()
admin.site.register(User, UserAdmin)
