from django.contrib import admin

# Register your models here.

from .models import Book, Author, Review


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'stock', 'price']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
