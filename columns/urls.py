from rest_framework.routers import DefaultRouter
from . import views

app_name = "features"
router = DefaultRouter()
router.register("", views.ColumnViewSet)


urlpatterns = router.urls
