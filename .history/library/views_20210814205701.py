from django.shortcuts import render
from django.views import generic

# Create your views here.

class IndexViewList(generic.ListView):
    model = Book
    