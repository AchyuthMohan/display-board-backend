from django.shortcuts import render
from requests import Response
from rest_framework import generics
from yaml import serialize
# from sqlalchemy import true
from .models import product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view

class ProductList(generics.ListCreateAPIView):
    queryset=product.objects.all()
    serializer_class=ProductSerializer
    