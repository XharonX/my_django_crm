from django.shortcuts import render
from .models import Product, Specification
from rest_framework import viewsets
from .serializers import ProductSerializer
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
   queryset = Product.objects.all().order_by('product_code')
   serializer_class = ProductSerializer
