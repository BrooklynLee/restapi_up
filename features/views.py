from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import permissions
from .models import Feature
from .serializers import FeatureSerializer
from .permissions import IsOwner


class FeatureViewSet(ModelViewSet):

    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [permissions.AllowAny]
        elif self.action == "create":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    @action(detail=False)
    def search(self, request):
        max_price = request.GET.get("max_price", None)
        min_price = request.GET.get("min_price", None)
        beds = request.GET.get("beds", None)
        bedrooms = request.GET.get("bedrooms", None)
        bathrooms = request.GET.get("bathrooms", None)
        lat = request.GET.get("lat", None)
        lng = request.GET.get("lng", None)
        filter_kwargs = {}
        if max_price is not None:
            filter_kwargs["price__lte"] = max_price
        if min_price is not None:
            filter_kwargs["price__gte"] = min_price
        if beds is not None:
            filter_kwargs["beds__gte"] = beds
        if bedrooms is not None:
            filter_kwargs["bedrooms__gte"] = bedrooms
        if bathrooms is not None:
            filter_kwargs["bathrooms__gte"] = bathrooms
        paginator = self.paginator
        if lat is not None and lng is not None:
            filter_kwargs["lat__gte"] = float(lat) - 0.005
            filter_kwargs["lat__lte"] = float(lat) + 0.005
            filter_kwargs["lng__gte"] = float(lng) - 0.005
            filter_kwargs["lng__lte"] = float(lng) + 0.005
        try:
            features = Feature.objects.filter(**filter_kwargs)
        except ValueError:
            features = Feature.objects.all()
        results = paginator.paginate_queryset(features, request)
        serializer = FeatureSerializer(results, many=True)
        return paginator.get_paginated_response(serializer.data)