from rest_framework.viewsets import ModelViewSet

# from rest_framework.decorators import action
from rest_framework import permissions
from .models import Notice
from .serializers import NoticeSerializer


class NoticeViewSet(ModelViewSet):

    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
