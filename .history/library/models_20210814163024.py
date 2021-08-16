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
        return available == False

    def place(self):
        

class PlaceOfTheBook(models.Model):
    number_of_the_room = models.IntegerField(max_length=3)
    shelf_identificator = models.CharField(max_length=15)
