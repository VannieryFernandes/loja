from rest_framework import routers
from .viewsets import ProdutoViewSet

router = routers.SimpleRouter()
router.register(r'', ProdutoViewSet,basename='produto')
urlpatterns = router.urls