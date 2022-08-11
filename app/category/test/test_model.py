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

    def test_create_category_withot_name_raises_error(self):
        with self.assertRaises(Exception):
            Category.objects.create(
                name=None)

    def test_create_category_with_existing_name_raises_error(self):
        with self.assertRaises(Exception):
            Category.objects.create(
                name=Category.objects.get(id=1).name)

    def test_create_category_withot_category_type_raises_error(self):
        with self.assertRaises(Exception):
            Category.objects.create(
                name='Some', category_type=None)

    def test_create_new_category(self):
        Category.objects.create(name='Category 5', category_type='P', icon='icon 5',
                                description='Category 5 description', parent=Category.objects.get(id=4)
                                )
        self.assertEqual(Category.objects.count(), 5)
        self.assertEqual(Category.objects.last().name, 'Category 5')
        self.assertEqual(Category.objects.last().slug, 'category-5')
        self.assertEqual(Category.objects.last().icon, 'icon 5')
        self.assertEqual(Category.objects.last().category_type, 'P')
        self.assertEqual(Category.objects.last().description,
                         'Category 5 description')
        self.assertEqual(Category.objects.last().parent,
                         Category.objects.get(id=4))

    def test_update_category(self):
        category = Category.objects.get(id=1)
        category.name = 'New name'
        category.icon = 'new icon'
        category.description = 'New description'
        category.category_type = 'E'
        category.is_enabled = False
        category.parent = Category.objects.get(id=2)
        category.save()

        self.assertEqual(Category.objects.get(id=1).name, 'New name')
        self.assertEqual(Category.objects.get(id=1).slug, 'new-name')
        self.assertEqual(Category.objects.get(id=1).icon, 'new icon')
        self.assertEqual(Category.objects.get(
            id=1).description, 'New description')
        self.assertEqual(Category.objects.get(id=1).category_type, 'E')
        self.assertEqual(Category.objects.get(id=1).is_enabled, False)
        self.assertEqual(Category.objects.get(
            id=1).parent, Category.objects.get(id=2))

    def test_delete_category(self):
        Category.objects.get(id=3).delete()
        self.assertEqual(Category.objects.count(), 3)
