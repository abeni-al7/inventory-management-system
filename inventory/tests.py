from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Suppliers, Categories, Manufacturer


class SuppliersAPITestCase(APITestCase):
    def setUp(self):
        self.supplier = Suppliers.objects.create(name='Supplier1', phone='912345678')
        self.url = reverse('suppliers-list') 

    def test_create_supplier(self):
        """Test creating a new supplier."""
        data = {'name': 'Supplier2', 'phone': '998765432'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Suppliers.objects.count(), 2)
        self.assertEqual(Suppliers.objects.get(id=response.data['id']).name, 'Supplier2')

    def test_get_supplier_list(self):
        """Test retrieving the list of suppliers."""
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_supplier_detail(self):
        """Test retrieving a single supplier by ID."""
        url = reverse('suppliers-detail', args=[self.supplier.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.supplier.name)

    def test_update_supplier(self):
        """Test updating an existing supplier."""
        url = reverse('suppliers-detail', args=[self.supplier.id])
        data = {'name': 'UpdatedSupplier', 'phone': '712345678'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.supplier.refresh_from_db()
        self.assertEqual(self.supplier.name, 'UpdatedSupplier')

    def test_delete_supplier(self):
        """Test deleting a supplier."""
        url = reverse('suppliers-detail', args=[self.supplier.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Suppliers.objects.count(), 0)


class CategoriesAPITestCase(APITestCase):
    def setUp(self):
        self.category = Categories.objects.create(name='Category1', description='Description1')
        self.url = reverse('categories-list')  # Ensure this matches your router name

    def test_create_category(self):
        """Test creating a new category."""
        data = {'name': 'Category2', 'description': 'Description2'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Categories.objects.count(), 2)
        self.assertEqual(Categories.objects.get(id=response.data['id']).name, 'Category2')

    def test_get_category_list(self):
        """Test retrieving the list of categories."""
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_category_detail(self):
        """Test retrieving a single category by ID."""
        url = reverse('categories-detail', args=[self.category.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.category.name)

    def test_update_category(self):
        """Test updating an existing category."""
        url = reverse('categories-detail', args=[self.category.id])
        data = {'name': 'UpdatedCategory', 'description': 'Updated Description'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, 'UpdatedCategory')

    def test_delete_category(self):
        """Test deleting a category."""
        url = reverse('categories-detail', args=[self.category.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Categories.objects.count(), 0)


class ManufacturerAPITestCase(APITestCase):
    def setUp(self):
        self.manufacturer = Manufacturer.objects.create(name='Manufacturer1', logo_url='https://example.com/logo', type='Infrastructure')
        self.url = reverse('manufacturer-list')  # Ensure this matches your router name

    def test_create_manufacturer(self):
        """Test creating a new manufacturer."""
        data = {'name': 'Manufacturer2', 'country': 'Country2'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Manufacturer.objects.count(), 2)
        self.assertEqual(Manufacturer.objects.get(id=response.data['id']).name, 'Manufacturer2')

    def test_get_manufacturer_list(self):
        """Test retrieving the list of manufacturers."""
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_manufacturer_detail(self):
        """Test retrieving a single manufacturer by ID."""
        url = reverse('manufacturer-detail', args=[self.manufacturer.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.manufacturer.name)

    def test_update_manufacturer(self):
        """Test updating an existing manufacturer."""
        url = reverse('manufacturer-detail', args=[self.manufacturer.id])
        data = {'name': 'UpdatedManufacturer', 'country': 'UpdatedCountry'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.manufacturer.refresh_from_db()
        self.assertEqual(self.manufacturer.name, 'UpdatedManufacturer')

    def test_delete_manufacturer(self):
        """Test deleting a manufacturer."""
        url = reverse('manufacturer-detail', args=[self.manufacturer.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Manufacturer.objects.count(), 0)
