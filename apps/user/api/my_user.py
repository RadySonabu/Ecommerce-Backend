from ..models import  MyUser
from rest_framework import viewsets
from ..serializers.my_user import *
from django_filters import rest_framework as filters



class MyUserView(viewsets.ModelViewSet):
	queryset=MyUser.objects.select_related().all()
	serializer_class=OutputMyUserSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	def get_serializer_class(self):
		input_serializer = InputMyUserSerializer
		output_serializer = OutputMyUserSerializer
		if self.action == 'list':
			return output_serializer
		if self.action == 'retrieve':
			return output_serializer
		if self.action == 'create':
			return input_serializer
		if self.action == 'update':
			return input_serializer

		return output_serializer
                    