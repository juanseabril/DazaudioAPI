from rest_framework import serializers
from InventaryApp.models import Products

class ProductSerializer(serializers.ModelSerializer):
     class Meta:
          model = Products
          fields = ('ProductId', 'ProductName', 'ProductBuy', 'ProductSell')
