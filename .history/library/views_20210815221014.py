from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book, PlaceOfTheBook
from django.http import HttpResponse

class IndexViewList(generic.ListView):
    template_name = "library/index.html"
    context_object_name = "books_list"

    def get_queryset(request):
        return Book.objects.get.all()

class BookInfoDetailView(generic.DetailView):
    model = Book
    template_name = "library/detail.html"

    def check_books(request, identificator):
        book = get_object_or_404(Book, pk=identificator)
        selected_book = book.place_set.get(pk=request.GET['identificator_of_the_book'])
        return render(request, "library/detail.html", {"available": available})

def book_a_book(request, identificator):
    book = get_object_or_404(Book, identificator)
    selected_book = book.place_set.get(pk=request.GET['place'])
    selected_book.available = False
    selected_book.save()
    return HttpResponse(reverse("library:book-a-book-results"))

class BookABookResults()