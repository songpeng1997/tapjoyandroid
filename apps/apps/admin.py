from django.contrib import admin
from apps.models import Category, SubCategory, App, AppDownload, CarouselApp


class AppDownloadAdmin(admin.ModelAdmin):
    list_display = ('app', 'count',)

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(App)
admin.site.register(AppDownload, AppDownloadAdmin)
admin.site.register(CarouselApp)
