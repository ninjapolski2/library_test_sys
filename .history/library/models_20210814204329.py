from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    identificator = models.CharField(max_length=12)
    available = models.BooleanField('dostępność', default=True)

    def __str__(self):
        return self.author+": "+self.title

    def is_lent(self):
        return available == T

class PlaceOfTheBook(models.Model):
    identificator_of_the_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number_of_the_room = models.IntegerField(default=0)
    shelf_identificator = models.CharField(max_length=15)
    def __str__(self):
        return self.identificator_of_the_book + " - " + self.number_of_the_room + " | " + self.shelf_identificator