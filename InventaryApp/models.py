from django.db import models

# Create your models here.
class Products(models.Model):
    ProductId = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=500)
    ProductBuy = models.CharField(max_length=500)
    ProductSell = models.CharField(max_length=500)
