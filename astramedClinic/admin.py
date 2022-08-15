from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from astramedClinic.models import Photos, Links, Services, Employee, Reviews, Blog, Users


class BlogAdminForm(forms.ModelForm):
    description = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())
    links = forms.CharField(label='Источники', widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'


class ServicesAdminForm(forms.ModelForm):
    title = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Services
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = BlogAdminForm


class ServicesAdmin(admin.ModelAdmin):
    form = ServicesAdminForm


admin.site.register(Photos)
admin.site.register(Links)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Employee)
admin.site.register(Reviews)
admin.site.register(Users)
admin.site.register(Blog, PostAdmin)
