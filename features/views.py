from rest_framework.viewsets import ModelViewSet

# from rest_framework.decorators import action
from rest_framework import permissions
from .models import Feature
from .serializers import FeatureSerializer
from .permissions import IsOwner
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class FeatureViewSet(ModelViewSet):

    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ["feature_type", "tag"]
    search_fields = ["name"]

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [permissions.AllowAny]
        elif self.action == "create":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    # @action(detail=False)
    # def search(self, request):
    #     name = request.GET.get("search_word", None)
    #     print(name)
    #     # min_price = request.GET.get("min_price", None)
    #     # beds = request.GET.get("beds", None)
    #     # bedrooms = request.GET.get("bedrooms", None)
    #     # bathrooms = request.GET.get("bathrooms", None)
    #     # lat = request.GET.get("lat", None)
    #     # lng = request.GET.get("lng", None)
    #     filter_kwargs = {}
    #     # if max_price is not None:
    #     #     filter_kwargs["price__lte"] = max_price
    #     # if min_price is not None:
    #     #     filter_kwargs["price__gte"] = min_price
    #     # if beds is not None:
    #     #     filter_kwargs["beds__gte"] = beds
    #     # if bedrooms is not None:
    #     #     filter_kwargs["bedrooms__gte"] = bedrooms
    #     # if bathrooms is not None:
    #     #     filter_kwargs["bathrooms__gte"] = bathrooms
    #     paginator = self.paginator
    #     try:
    #         features = Feature.objects.filter(**filter_kwargs)
    #     except ValueError:
    #         features = Feature.objects.all()
    #     results = paginator.paginate_queryset(features, request)
    #     serializer = FeatureSerializer(results, many=True)
    #     return paginator.get_paginated_response(serializer.data)
