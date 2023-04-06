from django.views.generic import ListView

from books.models import Book


class HomeView(ListView):
    queryset = Book.objects.order_by("-id")
    template_name = "home.html"
    context_object_name = "books"
