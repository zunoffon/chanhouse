from django.contrib import admin
from .models import User, Category, BookDate

from import_export.admin import ImportExportModelAdmin, ImportExportMixin, ImportMixin
from import_export import resources


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'job', 'email', 'facebook')
    list_filter = ('name', 'phone')
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('typename', 'price_normal')
    list_display = ('typename', 'price_normal', 'price_student', 'price_staff', 'price_vip')


class BookDateResource(resources.ModelResource):
    class Meta:
        model = BookDate


@admin.register(BookDate)
class BookDateAdmin(ImportExportModelAdmin):
    list_display = ('user', 'orderDate', 'category', 'status')


