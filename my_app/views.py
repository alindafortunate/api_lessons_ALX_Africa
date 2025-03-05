from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


# Create your views here.
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def get_queryset(self):
    #     queryset = self.queryset
    #     name_filter = self.request.query_params.get("Java")
    #     if name_filter is not None:
    #         queryset = queryset.filter(title_icontains=name_filter)

    #     return queryset

    def get_queryset(self):
        queryset = self.queryset

        queryset = queryset.filter(title__icontains="Java")

        return queryset


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
