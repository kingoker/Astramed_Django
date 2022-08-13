from django.contrib import admin

# Register your models here.


from astramedClinic.models import Photos, Links, Services, Employee, Reviews, Blog, Users

admin.site.register(Photos)
admin.site.register(Links)
admin.site.register(Services)
admin.site.register(Employee)
admin.site.register(Reviews)
admin.site.register(Users)
admin.site.register(Blog)