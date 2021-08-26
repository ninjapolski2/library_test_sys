from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book, Place
from django.http import HttpResponse
from . import views

place = Place()
class IndexViewList(generic.ListView):
    template_name = "index.html"
    context_object_name = "books_list"

    def get_queryset(request):
        return Book.objects.all()

class BookInfoDetailView(generic.DetailView):
    model = Book
    template_name = "detail.html"

class BookABookResultsView(generic.DetailView):
    model = Book
    template_name = "book-a-book-results.html"

def book_a_book(request, identificator):
    book = get_object_or_404(Book, identificator)
    selected_book = book.place_set.get(pk=request.GET['place'])
    selected_book.available = False
    selected_book.save()
    return HttpResponse(reverse("library:book-a-book-results", args=(book.pk)))
