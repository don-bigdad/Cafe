from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Specials)
admin.site.register(AboutUs)


@admin.register(Dish)
class AdminDish(admin.ModelAdmin):
    list_filter = ('in_category',)
    prepopulated_fields = {"slug":("name",),}

@admin.register(Event)
class AdminDish(admin.ModelAdmin):
    list_filter = ('name',)
    prepopulated_fields = {"slug": ("name",), }
