from ..serializers.my_user import RegisterUserSerializer, OutputMyUserSerializer 
from rest_framework import  generics
from rest_framework.response import Response


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": OutputMyUserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })