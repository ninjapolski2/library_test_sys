from django.db import models
from django.utils import timezone
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    identificator = models.CharField(max_length=12)
    availability = models.BooleanField('dostępność', default=True)
    pub_date = models.DateTimeField('data publikacji książki', default=timezone.now())

    def __str__(self):
        return self.author+": "+self.title

    def is_available(self):
        return availability == True

class Place(models.Model):
    identificator_of_the_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    shelf_identificator = models.CharField(max_length=15)
    filia = models.IntegerField(max_length=2)
    adress = models.TextField(max_length=1000)
    availability = models.BooleanField('dostępność', default=True)
    def __str__(self):
        return self.identificator_of_the_book + "-" + self.shelf_identificator