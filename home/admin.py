from django.contrib import admin
# Register your models here.
from .models import Addmoney_info
from django.contrib.sessions.models import Session
from .models import UserProfile

class Addmoney_infoAdmin(admin.ModelAdmin):
    list_display=("user","quantity","Date","Category","add_money")
admin.site.register(Addmoney_info,Addmoney_infoAdmin)


admin.site.register(Session)
admin.site.register(UserProfile)
