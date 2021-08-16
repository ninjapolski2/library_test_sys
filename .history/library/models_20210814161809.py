from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    identificator = models.CharField(max_length=12)
    available = models.BooleanField('dostępn'default=True)

    def is_lent(self):
        return available is False

