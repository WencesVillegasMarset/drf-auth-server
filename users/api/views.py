from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from users.api.serializers import RegistrationSerializer
# from rest_framework import viewsets
# from django.contrib.auth.models import Group
from users.permissions import RoleBasedPermission


@api_view(['POST'])
@permission_classes([RoleBasedPermission])
def user_add(request):
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


# @permission_classes([RoleBasedPermission])
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializer_class = GroupSerializer
#     queryset = Group.objects.all()
