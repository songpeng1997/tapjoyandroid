from django.contrib import admin
from apps.models import Category, SubCategory, App, AppDownload, CarouselApp

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(App)
admin.site.register(AppDownload)
admin.site.register(CarouselApp)