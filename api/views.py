from django.shortcuts import render
from rest_framework.generics import ListAPIView

from api.serializers import ProductsModelSerializer
from products.models import ProductsModel


class ProductListAPIView(ListAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsModelSerializer
