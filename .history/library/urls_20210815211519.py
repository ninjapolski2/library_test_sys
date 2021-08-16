from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexViewList.as_view())
]
