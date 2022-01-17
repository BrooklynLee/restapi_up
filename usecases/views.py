from rest_framework.viewsets import ModelViewSet

# from rest_framework.decorators import action
from rest_framework import permissions
from .models import Usecase
from .serializers import UsecaseSerializer


class UsecaseViewSet(ModelViewSet):

    queryset = Usecase.objects.all()
    serializer_class = UsecaseSerializer
