from rest_framework.routers import SimpleRouter

from shops.views import ShopViewSet

router = SimpleRouter()

router.register('', ShopViewSet)

urlpatterns = router.urls
