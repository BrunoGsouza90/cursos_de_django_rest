from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets
from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):

    """
    Endpoint da API que permite visualizar ou editar usuários.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):

    """
    Endpoint da API que permite visualizar ou editar grupos.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]