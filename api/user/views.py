from rest_framework import viewsets

from user.models import User
from serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
