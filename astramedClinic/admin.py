from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from astramedClinic.models import Links, Services, Employee, Reviews, Blog, MainPage, UnderServices, \
    CategoryBlog, Info, Applications, PriceList, Jobs, Partners, Contacs, AboutPage, CooperationPage, ServicesPage, \
    PhilosBlog, ServicePhoto


# Удобная админ панель
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published')
    list_display_links = ('title', )
    search_fields = ('title', 'description', )
    list_editable = ('published', 'category')
    save_on_top = True


class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'therapy', 'date', 'status', )
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


class AdminServices(admin.ModelAdmin):
    list_display = ('type', 'sort', 'published',)
    list_display_links = ('type', )
    list_filter = ('sort', 'published', )
    list_editable = ('sort', 'published', )

    class Meta:
        model = Applications
        fields = '__all__'


class ServicePhotoAdmin(admin.ModelAdmin):
    list_display = ('therapy', 'get_photo', 'published',)
    list_editable = ('published',)

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.Photo.url}" width="200px" height="100px">')

    class Meta:
        model = ServicePhoto
        fields = '__all__'


admin.site.register(Links)
admin.site.register(ServicePhoto, ServicePhotoAdmin)
admin.site.register(CooperationPage)
admin.site.register(AboutPage)
admin.site.register(PhilosBlog)
admin.site.register(ServicesPage)
admin.site.register(Services, AdminServices)
admin.site.register(Employee)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Blog, PostAdmin)
admin.site.register(MainPage)
admin.site.register(UnderServices)
admin.site.register(CategoryBlog)
admin.site.register(Info)
admin.site.register(Applications, ApplicationsAdmin)
admin.site.register(PriceList)
admin.site.register(Jobs)
admin.site.register(Partners)
admin.site.register(Contacs)
