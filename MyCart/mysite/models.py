from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 20)
    address = models.TextField(max_length = 50)
    email = models.EmailField()
    
    def __str__(self):
        return self.label
        
class Product(models.Model):
    name = models.CharField(max_length = 20)
    quantity = models.PositiveIntegerField()
    brand = models.CharField(max_length = 20)