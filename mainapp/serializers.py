from dataclasses import field
from pyexpat import model
from numpy import product, source
from rest_framework import serializers
from .models import product
from mainapp import views
# class SnippetSerializer(serializers.ModelSerializer):
#     owner=serializers.ReadOnlyField(source='owner.username')
#     class Meta:
#         model=Snippet
#         fields=['id','title','code','linenos','language','owner']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=['id','name','price','img']