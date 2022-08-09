from django.contrib import admin

# Register your models here.
from astramedClinic.models import Photos, Links, Services, Employee

admin.site.register(Photos)
admin.site.register(Links)
admin.site.register(Services)
admin.site.register(Employee)