from .serializers import ProductSerializer
from productions.models import Product
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
   queryset = Product.objects.all().order_by('product_code')
   serializer_class = ProductSerializer

