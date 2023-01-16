from django.contrib import admin
from API.models import Profile
@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['name','email','DOB','State','location','pimage','gender','rdoc']

