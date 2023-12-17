from django.urls import path, include
from .views import ProductViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('product', ProductViewSet)
urlpatterns = [
   path('', include(router.urls)),
   path('products', include('rest_framework.urls', namespace='rest_framework'))
]
