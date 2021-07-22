from ..models import  Product
from rest_framework import viewsets
from ..serializers.product import *
from django_filters import rest_framework as filters



class ProductView(viewsets.ModelViewSet):
	queryset=Product.objects.select_related().all()
	serializer_class=OutputProductSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	def get_serializer_class(self):
		input_serializer = InputProductSerializer
		output_serializer = OutputProductSerializer
		if self.action == 'list':
			return output_serializer
		if self.action == 'retrieve':
			return output_serializer
		if self.action == 'create':
			return input_serializer
		if self.action == 'update':
			return input_serializer

		return output_serializer
                    