from django.urls import path
from .views import BookListCreateAPIView, BookListAPIView

urlpatterns = [
    path("api/books/", BookListAPIView.as_view(), name="book-list"),
    path("api/book/", BookListCreateAPIView.as_view(), name="book-list-create"),
]
