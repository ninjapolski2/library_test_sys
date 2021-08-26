from django.contrib import admin
from .models import Book, Place 

class BookAdmin(admin.ModelAdmin):
    fields = ['author', 'title', "identificator"]

class PlaceAdmin(admin.ModelAdmin):
    fieldsets = [["Biblioteka", ["filia", "adress"]]]
admin.site.register(Book, BookAdmin)
admin.site.register(Place)
# Register your models here.
