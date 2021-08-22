from django.contrib import admin
from .models import Book, Place 

class BookAdmin(admin.ModelAdmin):
    fields = ['author', 'title']

admin.site.register(Book, BookAdmin)
admin.site.register()
# Register your models here.
