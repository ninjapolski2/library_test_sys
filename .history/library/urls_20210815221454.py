from django.urls import path
from . import views
from .models import Book, Place

urlpatterns = [
    path("", views.IndexViewList.as_view(), name="index"),
    path("<int:pk>/", views.BookInfoDetailView.as_view(), name="detail"),
    path("<int:identificator_of_the_book>/book-a-book/", views.book_a_book, name="book-a-book"),
    path("<int:pk>/book-a-book/book-a-book/results/", views.BookABookResultsView.as_view(), name="book-a-book-results-view"
    
]
