from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from astramedClinic.models import Links, Services, Employee, Reviews, Blog, MainPage, UnderServices, \
    CategoryBlog, Info, Applications, PriceList, Jobs, Partners, Contacs, AboutPage, CooperationPage


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


class UnderServicesAdminForm(forms.ModelForm):
    title = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = UnderServices
        fields = '__all__'


class UnderServicesAdmin(admin.ModelAdmin):
    form = UnderServicesAdminForm


class AddInfoAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Info
        fields = '__all__'


class InfoAdmin(admin.ModelAdmin):
    form = AddInfoAdminForm


admin.site.register(Links)
admin.site.register(CooperationPage)
admin.site.register(AboutPage)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Employee)
admin.site.register(Reviews)
admin.site.register(Blog, PostAdmin)
admin.site.register(MainPage)
admin.site.register(UnderServices, UnderServicesAdmin)
admin.site.register(CategoryBlog)
admin.site.register(Info, InfoAdmin)
admin.site.register(Applications)
admin.site.register(PriceList)
admin.site.register(Jobs)
admin.site.register(Partners)
admin.site.register(Contacs)
