from .views import SuppliersViewSet, CategoriesViewSet, ManufacturerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'suppliers', SuppliersViewSet)
router.register(r'categories', CategoriesViewSet)
router.register(r'manufacturer', ManufacturerViewSet)
urlpatterns = router.urls