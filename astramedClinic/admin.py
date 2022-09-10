from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from astramedClinic.models import Links, Services, Employee, Reviews, Blog, MainPage, UnderServices, \
    CategoryBlog, Info, Applications, PriceList, Jobs, Partners, Contacs, AboutPage, CooperationPage, ServicesPage, \
    PhilosBlog


# CKeditor
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


class UnderServicesAdminForm(forms.ModelForm):
    title = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = UnderServices
        fields = '__all__'


class AddInfoAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Info
        fields = '__all__'


# Удобная админ панель
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published')
    list_display_links = ('title', )
    search_fields = ('title', 'description', )
    list_editable = ('published', 'category')
    form = BlogAdminForm
    save_on_top = True


class ServicesAdmin(admin.ModelAdmin):
    form = ServicesAdminForm


class UnderServicesAdmin(admin.ModelAdmin):
    form = UnderServicesAdminForm


class InfoAdmin(admin.ModelAdmin):
    form = AddInfoAdminForm


class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'therapy', 'date', 'finish_date', 'status', )
    list_display_links = ('name', )
    list_filter = ('status', 'therapy')
    search_fields = ('name', )
    list_editable = ('status', )
    class Meta:
        model = Applications
        fields = '__all__'


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'published',)
    list_display_links = ('name', )
    list_filter = ('published', )
    search_fields = ('name', 'description',)
    list_editable = ('published', )
    class Meta:
        model = Applications
        fields = '__all__'


admin.site.register(Links)
admin.site.register(CooperationPage)
admin.site.register(AboutPage)
admin.site.register(PhilosBlog)
admin.site.register(ServicesPage)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Employee)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Blog, PostAdmin)
admin.site.register(MainPage)
admin.site.register(UnderServices, UnderServicesAdmin)
admin.site.register(CategoryBlog)
admin.site.register(Info, InfoAdmin)
admin.site.register(Applications, ApplicationsAdmin)
admin.site.register(PriceList)
admin.site.register(Jobs)
admin.site.register(Partners)
admin.site.register(Contacs)
