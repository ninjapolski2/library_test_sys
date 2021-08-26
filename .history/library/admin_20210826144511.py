from django.contrib import admin
from .models import Book, Place 

class BookAdmin(admin.ModelAdmin):
    fields = ['author', 'title', "identificator"]

class PlaceAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Biblioteka", {"fields": ["filia", "adress", "shelf_identificator"]}),
        (None, {"fields": ["availability"}),
    ]

admin.site.register(Book, BookAdmin)
admin.site.register(Place, PlaceAdmin)
# Register your models here.
