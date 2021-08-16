from django.shortcuts import render
from django.views import generic
from .models import 

# Create your views here.

class IndexViewList(generic.ListView):
    template_name = "library/index.html"
    context_object_name = "books_list"

    def get_queryset(self):
        return Book.objects.filter('-author')

class BookDetailView(generic.DetailView):
    model = 
    pass