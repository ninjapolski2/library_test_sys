from django.contrib import admin
from .models import Book, Place 

class BookAdmin(admin.ModelAdmin):
    fields = [''

    ]

admin.site.register(Question)
# Register your models here.
