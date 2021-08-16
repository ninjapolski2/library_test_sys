from django.shortcuts import render
from django.views import generic
from .models import Book, PlaceOfTheBook

# Create your views here.

class IndexViewList(generic.ListView):
    template_name = "library/index.html"
    context_object_name = "books_list"

    def get_queryset(self):
        return Book.objects.filter('-author')

class BookInfoDetailView(generic.DetailView):
    model = Book
    template_name = "library/detail.html"

class BookABookView(generic.DetailView):
    model = PlaceOfTheBook
    template_name