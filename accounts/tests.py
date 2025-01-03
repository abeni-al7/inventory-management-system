from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCRUDAPITestCase(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            phone='912345678',
            password='adminpass123'
        )
        self.client.login(username='admin', password='adminpass123')
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'phone': '912345432',
            'password': 'testpass123'
        }

    def test_create_user(self):
        """Test creating a new user."""
        url = reverse('user-list')
        response = self.client.post(url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(username='testuser').email, 'testuser@example.com')

    def test_list_users(self):
        """Test retrieving the list of users."""
        url = reverse('user-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_user(self):
        """Test retrieving a single user by ID."""
        user = User.objects.get(username='admin')
        url = reverse('user-detail', args=[user.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'admin')

    def test_update_user(self):
        """Test updating an existing user."""
        user = User.objects.get(username='admin')
        url = reverse('user-detail', args=[user.id])
        data = {'username': 'admin_updated', 'email': 'admin_updated@example.com', 'phone': '987654321'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user.refresh_from_db()
        self.assertEqual(user.username, 'admin_updated')
        self.assertEqual(user.email, 'admin_updated@example.com')

    def test_delete_user(self):
        """Test deleting a user."""
        user = User.objects.get(username='admin')
        url = reverse('user-detail', args=[user.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)