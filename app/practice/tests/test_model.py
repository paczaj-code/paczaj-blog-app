from django.test import TestCase
from blog.models import Post, Category
from practice.models import Practice
from freezegun import freeze_time
import datetime
# Create your tests here.


@freeze_time("2022-03-22")
class PracticeTest(TestCase):

    def setUp(self):

        Category.objects.create(
            name='Category 1', icon='icon1', description='description 1')
        Category.objects.create(
            name='Category 2', icon='icon2', description='description 2', )

        Post.objects.create(
            title='Post 1', category=Category.objects.first(), content='Post 1 content')
        Post.objects.create(
            title='Post 2', category=Category.objects.last(), content='Post 2 content')

        Practice.objects.create(
            name='Practice 1', category=Category.objects.first(),
            exercise='Exercice 1', solution='Solution exercise 1')
        Practice.objects.first().related_posts.add(Post.objects.first())
        Practice.objects.first().related_posts.add(Post.objects.last())

    def test_create_practice_successfully(self):
        self.assertEqual(Practice.objects.all().count(), 1)
        self.assertEqual(Practice.objects.first().name, 'Practice 1')
        self.assertEqual(Practice.objects.first().slug, 'practice-1')
        self.assertEqual(Practice.objects.first().exercise, 'Exercice 1')
        self.assertEqual(Practice.objects.first().category.name, 'Category 1')
        self.assertEqual(Practice.objects.first().category.slug, 'category-1')
        self.assertEqual(Practice.objects.first().solution,
                         'Solution exercise 1')
        self.assertEqual(
            Practice.objects.first().related_posts.count(), 2)
        self.assertEqual(
            Practice.objects.first().related_posts.first().title, 'Post 1')
        self.assertEqual(
            Practice.objects.first().related_posts.last().title, 'Post 2')
        self.assertEqual(
            Practice.objects.first().created_at, datetime.datetime(2022, 3, 22, 0, 0, tzinfo=datetime.timezone.utc))
        self.assertEqual(
            Practice.objects.last().modified_at, datetime.datetime(2022, 3, 22, 0, 0, tzinfo=datetime.timezone.utc))

    def test_create_practice_without_name_raises_error(self):
        with self.assertRaises(Exception):
            Practice.objects.create(
                name=None, category=Category.objects.first(),
                exercise='Exercice 1', solution='Solution exercise 1')

    def test_create_practice_without_category_raises_error(self):
        with self.assertRaises(Exception):
            Practice.objects.create(
                name='Some practse', category=None,
                exercise='Exercice 1', solution='Solution exercise 1')

    def test_update_practise_successfully(self):
        practise = Practice.objects.first()
        practise.name = 'New name'
        practise.exercise = 'New exercise'
        practise.solution = 'New solution'
        practise.category = Category.objects.last()
        practise.related_posts.remove(Post.objects.first())
        practise.save()

        self.assertEqual(Practice.objects.all().count(), 1)
        self.assertEqual(Practice.objects.first().name, 'New name')
        self.assertEqual(Practice.objects.first().slug, 'new-name')
        self.assertEqual(Practice.objects.first().exercise, 'New exercise')
        self.assertEqual(Practice.objects.first().category.name, 'Category 2')
        self.assertEqual(Practice.objects.first().category.slug, 'category-2')
        self.assertEqual(Practice.objects.first().related_posts.count(), 1)
        self.assertEqual(Practice.objects.first(
        ).related_posts.first().title, 'Post 2')

    def test_delete_practise_successfully(self):
        Practice.objects.first().delete()
        self.assertEqual(Practice.objects.all().count(), 0)
