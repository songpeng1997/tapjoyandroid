from django.contrib import admin
from apps.models import Category, SubCategory, App

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(App)