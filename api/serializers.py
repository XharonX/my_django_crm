from productions.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
      model = Product
      fields = ['product_code', 'product_name', 'product_price', 'product_warranty']

