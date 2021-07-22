from ..models import  *
from rest_framework import serializers
from rest_framework import viewsets

class InputProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product 
		fields='__all__'
		depth=4

class OutputProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product 
		fields=['id', 'date_created', 'date_modified', 'name', 'product_image', 'description', 'quantity', 'price']
		depth=4