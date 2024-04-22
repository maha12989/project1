from django.contrib import admin
from .models import Blood_group, Info

# Register your models here.
class BloodAdmin(admin.ModelAdmin) :
   list_display = ['blood_group']
admin.site.register(Blood_group, BloodAdmin)

class InfoAdmin(admin.ModelAdmin) :
   list_display = ['name', 'age', 'salary', 'blood_group']
admin.site.register(Info, InfoAdmin)