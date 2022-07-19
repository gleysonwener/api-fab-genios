from .views import ProdutoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'produto', ProdutoViewSet)
urlpatterns = router.urls
