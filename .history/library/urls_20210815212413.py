from django.urls import path
from . import views
from .models import Book, Place

urlpatterns = [
    path("", views.IndexViewList.as_view(), name="index"),
    path("<pk:identificator_of_the_book>/")
    
]
