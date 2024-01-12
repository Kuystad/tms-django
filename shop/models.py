from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)



