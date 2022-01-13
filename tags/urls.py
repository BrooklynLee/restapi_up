from rest_framework.routers import DefaultRouter
from . import views

app_name = "tags"
router = DefaultRouter()
router.register("", views.TagViewSet)


urlpatterns = router.urls
