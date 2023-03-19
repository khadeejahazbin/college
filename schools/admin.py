from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Department, Order


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Department, DepartmentAdmin)


# class OrderAdmin(admin, ModelAdmin):
#     list_display = ['name']
#     prepopulated_fields = {'name': ('name',)}
#
#
# admin.site.register(Order, ModelAdmin)
