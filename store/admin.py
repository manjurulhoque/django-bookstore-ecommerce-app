from django.contrib import admin

# Register your models here.

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'stock', 'price']


admin.site.register(Book, BookAdmin)
