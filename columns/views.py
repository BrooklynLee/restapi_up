from rest_framework.viewsets import ModelViewSet

# from rest_framework.decorators import action
from rest_framework import permissions
from .models import Column
from .serializers import ColumnSerializer


class ColumnViewSet(ModelViewSet):

    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
