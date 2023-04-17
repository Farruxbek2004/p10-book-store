from django.contrib import admin

from books.models import Book, BookAuthor, BookImage, Category, Tag, WishList


class BookImageInline(admin.TabularInline):
    model = BookImage
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [BookImageInline]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(BookImage)
class BookImageAdmin(admin.ModelAdmin):
    list_display = ["book", "image"]


admin.site.register(BookAuthor)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(WishList)
