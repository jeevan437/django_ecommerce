from django.db import models

# Create your models here.

class Stores(models.Model):

    name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 30)
    contact = models.CharField(max_length = 10)
    address = models.TextField(max_length = 50)
    reviews = models.IntegerField(null = True)

    def __str__(self):
        return self.name