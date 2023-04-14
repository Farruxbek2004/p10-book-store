from django.contrib import admin

from books.models import Book, Category, Author, Tag, WishList


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["category", "page_size"]


admin.site.register(WishList)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Category)
