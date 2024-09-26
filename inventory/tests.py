from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class ItemTests(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.token = self.obtain_jwt_token()

    def obtain_jwt_token(self):
        url = reverse('token_obtain_pair')
        response = self.client.post(url, data={
            'username': 'testuser',
            'password': 'testpassword'
        })
        return response.data['access']

    def test_create_item(self):
        url = reverse('item-list')
        data = {'name': 'Test Item', 'description': 'A test item'}
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_item(self):
        item = Item.objects.create(name='Test Item', description='A test item')
        url = reverse('item-detail', args=[item.id])
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        item = Item.objects.create(name='Test Item', description='A test item')
        url = reverse('item-detail', args=[item.id])
        data = {'name': 'Updated Item', 'description': 'Updated description.'}
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_item(self):
        item = Item.objects.create(name='Test Item', description='A test item')
        url = reverse('item-detail', args=[item.id])
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
