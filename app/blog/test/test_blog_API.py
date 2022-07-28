from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

CATEGORY_URL = reverse('blog:category-list')


class PublicCategoryAPITests(TestCase):
    """Tests for public API blog - categories"""
    fixtures = ['./fixtures/fixtures.json']

    def setUp(self):
        self.client = APIClient()

    def test_method_post_not_allowed(self):
        res = self.client.post(CATEGORY_URL)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_method_put_not_allowed(self):
        res = self.client.put(CATEGORY_URL)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_method_patch_not_allowed(self):
        res = self.client.put(CATEGORY_URL)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_list_of_categories_ok(self):
        res = self.client.get(CATEGORY_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], 'Category 1')
        self.assertEqual(res.data[0]['icon'], 'icon 1')
        self.assertEqual(res.data[0]['slug'], 'category-1')
        self.assertEqual(len(res.data[0]['subcategories']), 1)
        self.assertEqual(res.data[0]['subcategories'][0]['name'], 'Category 2')
        self.assertEqual(res.data[0]['subcategories'][0]['slug'], 'category-2')
        self.assertEqual(res.data[0]['subcategories'][0]['icon'], 'icon 2')
