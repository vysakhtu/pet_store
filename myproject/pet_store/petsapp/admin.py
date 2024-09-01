from django.contrib import admin
from .models import PetUser,Pet
# Register your models here.
# class PetAdmin(admin.ModelAdmin):
#     list_display=('id','name','gender','species','breed','age','description')
# admin.site.register(Pet,PetAdmin)
admin.site.register(Pet)
admin.site.register(PetUser)
