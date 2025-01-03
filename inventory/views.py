from .serializers import SuppliersSerializer, CategoriesSerializer, ManufacturerSerializer
from .models import Suppliers, Categories, Manufacturer
from rest_framework import viewsets


class SuppliersViewSet(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
