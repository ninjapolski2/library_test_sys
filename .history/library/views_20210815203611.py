from django.shortcuts import render
from django.views import generic
from .models import Book, PlaceOfTheBook
from django.shortcuts import get

# Create your views here.

class IndexViewList(generic.ListView):
    template_name = "library/index.html"
    context_object_name = "books_list"

    def get_queryset(request):
        return Book.objects.filter('-author')

class BookInfoDetailView(generic.DetailView):
    model = Book
    template_name = "library/detail.html"

def book_a_book(request, identificator):
    book = get_object_or_404
    selected_book = Book.
    pass