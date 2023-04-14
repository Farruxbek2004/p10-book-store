from django.contrib import admin

from .models import Author, Book, Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["category", "page_size"]


admin.site.register(Author)
admin.site.register(Category)
