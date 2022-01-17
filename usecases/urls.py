from rest_framework.routers import DefaultRouter
from . import views

app_name = "usecases"
router = DefaultRouter()
router.register("", views.FeatureViewSet)


urlpatterns = router.urls
