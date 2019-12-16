from django.db import models

# Create your models here.

available_choices = (
                    ('Y','yes'),
                     ('N','no')
                     )
class Stores(models.Model):

    name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 30)
    contact = models.CharField(max_length = 10)
    address = models.TextField(max_length = 50)
    reviews = models.IntegerField(null = True)

    def __str__(self):
        return self.name

class Products(models.Model):

    store =  models.ForeignKey(Stores, on_delete=models.CASCADE)
    name = models.CharField(max_length =30)
    location = models.TextField(max_length=50)
    price = models.IntegerField()
    manufactured_data = models.DateField()
    available = models.CharField(max_length = 5,choices = available_choices)

    def __str__(self):
        return self.name
