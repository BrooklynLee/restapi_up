from rest_framework.viewsets import ModelViewSet

# from rest_framework.decorators import action
from rest_framework import permissions
from .models import Tag
from .serializers import TagSerializer


class TagViewSet(ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
