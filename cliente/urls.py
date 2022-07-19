from .views import ClienteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ClienteViewSet)
urlpatterns = router.urls
