from rest_framework import viewsets
from .models import Feature
from .serializers import BigRoomSerializer


class FeatureViewset(viewsets.ModelViewSet):

    queryset = Feature.objects.all()
    serializer_class = BigRoomSerializer
