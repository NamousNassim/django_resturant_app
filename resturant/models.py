from django.db import models

# Create your models here.
class Book(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    number = models.IntegerField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.last_name
    
class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name