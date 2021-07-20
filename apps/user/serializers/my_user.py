from ..models import  *
from rest_framework import serializers
from rest_framework import viewsets

class InputMyUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = MyUser 
		fields='__all__'
		# exclude = ['last_login',  'username', 'is_superuser', 'is_staff', 'is_active', 'date_joined']
		depth=4

class OutputMyUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = MyUser 
		fields=['password', 'last_login', 'is_superuser', 'username', 'email', 'is_staff', 'is_active', 'date_joined', 'id', 'first_name', 'last_name', 'address', 'gcash_number']
		depth=4

class RegisterUserSerializer(serializers.ModelSerializer):

	class Meta:
		model = MyUser
		exclude = ['last_login',  'username', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions']
	
	def create(self, validated_data):
            user = MyUser.objects.create_user(
                username=validated_data['email'], 
                email= validated_data['email'], 
                first_name= validated_data['first_name'], 
                last_name= validated_data['last_name'], 
                gcash_number= validated_data['gcash_number'], 
                address= validated_data['address'],
                password=validated_data['password'], 
                )

            return user