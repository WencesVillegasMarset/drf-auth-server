from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from users.api.serializers import RegistrationSerializer


@api_view(['POST'])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = "Registration Successful"
        data['email'] = user.email
    else:
        data = serializer.errors
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    return Response(data=data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)
