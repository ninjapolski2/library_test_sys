from django.db import models
from django.utils import timezone
# Create your models here.
class Book(models.Model):
    title = models.CharField("tytuł", max_length=150)
    author = models.CharField("autor", max_length=100)
    description = models.TextField("opis", max_length=2000)
    identificator = models.CharField("identyfikator", max_length=12)
    
    def __str__(self):
        return self.author+": "+self.title

class Place(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    shelf_identificator = models.CharField("pokój|dział/półka", max_length=15)
    filia = models.IntegerField("filia")
    address = models.TextField("adres", max_length=1000)
    availability = models.BooleanField('dostępność', default=True)

    def __str__(self):
        return f"{self.identificator_of_the_book}"

    def is_available(self):
        return availability == True