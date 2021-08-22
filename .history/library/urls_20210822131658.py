from django.urls import path
from . import views
from .models import Book, Place

app_name = "library"
urlpatterns = [
    path("", views.IndexViewList.as_view(), name="index"),
    path("<pk:id>/", views.BookInfoDetailView.as_view(), name="detail"),
    path("<str:identificator>/book-a-book/", views.book_a_book, name="book-a-book"),
    path("<str:identificator>/book-a-book/results/", views.BookABookResultsView.as_view(), name="book-a-book-results-view"),
    
]
