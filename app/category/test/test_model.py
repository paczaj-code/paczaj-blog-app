from django.test import TestCase
from django.core.management import call_command
from category.models import Category


class CategoryTest(TestCase):
    """Test category model"""
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'fixtures/fixtures_new.json', verbosity=0)

    def test_inserted_fixtures(self):
        self.assertEqual(Category.objects.get(id=1).name, 'Category 1')
        self.assertEqual(Category.objects.get(id=1).slug, 'category-1')
        self.assertEqual(Category.objects.get(
            id=1).category_type, 'P')
        self.assertEqual(Category.objects.get(id=1).is_enabled, True)
        self.assertEqual(Category.objects.get(id=1).parent, None)
        self.assertEqual(Category.objects.get(
            id=1).description, "I'm category 1")

        self.assertEqual(Category.objects.get(id=4).category_type, 'E')
