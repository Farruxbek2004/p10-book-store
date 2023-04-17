from books.models import Book


def books_count(request):
    books = Book.objects.all()
    return {
        "books_count": books.count(),
    }