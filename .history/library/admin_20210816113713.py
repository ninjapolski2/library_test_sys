from django.contrib import admin
from .models import Book, Place 

class BookAdmin(admin.ModelAdmin):
    fields = ['author', 'title']

admin.site.register(Book, BookAdmin(model, admin_site))
# Register your models here.
