from django.contrib import admin
from .models import User, Category, BookDate


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


admin.site.register(BookDate)
