from django.db import models

# Create your models here.

class  Product (models.Model):
    Date = models.DateField()
    Provider = models.CharField(max_length=30)
    Product_name=models.CharField(max_length=60)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    Amount = models.FloatField()
    Stock = models.IntegerField()


