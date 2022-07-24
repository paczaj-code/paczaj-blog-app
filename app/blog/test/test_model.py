
from faulthandler import is_enabled
from nis import cat
from turtle import title
from unicodedata import category, name
from django.test import TestCase
from blog.models import Post, Category, Tag
from freezegun import freeze_time
import datetime
# Create your tests here.


@freeze_time("2022-07-14")
class CategoryTest(TestCase):
    def setUp(self):
        Category.objects.create(
            name='category1', icon='icon1', description='description 1')
        Category.objects.create(
            name='category2', icon='icon2', description='description 2', )
        Category.objects.create(
            name='category 3', icon='icon3', description='description 3',
            parent=Category.objects.first(),
            is_enabled=False
        )

    def test_categories_created_successfull(self):
        category_1 = Category.objects.first()
        category_2 = Category.objects.last()
        self.assertEqual(Category.objects.all().count(), 3)
        self.assertEqual(category_2.name, 'category 3')
        self.assertEqual(category_2.icon, 'icon3')
        self.assertEqual(category_2.slug, 'category-3')
        self.assertEqual(category_2.description, 'description 3')
        self.assertEqual(
            category_2.created_at, datetime.datetime(2022, 7, 14, 0, 0, tzinfo=datetime.timezone.utc))
        self.assertEqual(
            category_2.modified_at, datetime.datetime(2022, 7, 14, 0, 0, tzinfo=datetime.timezone.utc))

        self.assertEqual(category_2.parent, category_1)

    def test_create_category_with_missing_name_raises_error(self):
        with self.assertRaises(Exception):
            Category.objects.create(
                name=None, icon='icon1', description='description 1')

    def test_create_category_with_existing_name_raises_error(self):
        category = Category.objects.first()
        category.name = Category.objects.last().name
        with self.assertRaises(Exception):
            category.save()

    def test_update_category_successfull(self):
        category = Category.objects.last()
        category.name = 'New Name'
        category.save()
        self.assertEqual(Category.objects.last().name, 'New Name')
        self.assertEqual(Category.objects.last().slug, 'new-name')

    def test_delete_category_successfull(self):
        Category.objects.first().delete()
        self.assertEqual(Category.objects.count(), 2)


@freeze_time("2022-07-14")
class TagTest(TestCase):
    def setUp(self):
        Tag.objects.create(name='Tag 1', icon='Icon 1',
                           description='description 1')
        Tag.objects.create(name='Tag 2', icon='Icon 2',
                           description='description 2')

    def test_tags_created_successfully(self):
        self.assertEqual(Tag.objects.first().name, 'Tag 1')
        self.assertEqual(Tag.objects.first().slug, 'tag-1')
        self.assertEqual(Tag.objects.first().icon, 'Icon 1')
        self.assertEqual(Tag.objects.first().description, 'description 1')
        self.assertEqual(
            Tag.objects.first().created_at, datetime.datetime(2022, 7, 14, 0, 0, tzinfo=datetime.timezone.utc))
        self.assertEqual(
            Tag.objects.first().modified_at, datetime.datetime(2022, 7, 14, 0, 0, tzinfo=datetime.timezone.utc))

    def test_create_tag_with_missing_name_raises_error(self):
        with self.assertRaises(Exception):
            Tag.objects.create(name=None)

    def test_update_tag_with_existing_name_raises_error(self):
        with self.assertRaises(Exception):
            Tag.objects.create(name=Tag.objects.first().name)

    def test_update_tag_successfully(self):
        tag = Tag.objects.first()
        tag.name = 'New tag name'
        tag.icon = 'new icon'
        tag.description = 'new description'
        tag.save()
        self.assertEqual(Tag.objects.first().name, 'New tag name')
        self.assertEqual(Tag.objects.first().slug, 'new-tag-name')
        self.assertEqual(Tag.objects.first().icon, 'new icon')
        self.assertEqual(Tag.objects.first().description, 'new description')
        self.assertEqual(
            Tag.objects.first().created_at, datetime.datetime(2022, 7, 14, 0, 0, tzinfo=datetime.timezone.utc))
        self.assertEqual(
            Tag.objects.first().modified_at, datetime.datetime(2022, 7, 14, 0, 0, tzinfo=datetime.timezone.utc))

    def test_delete_tag_successfully(self):
        Tag.objects.first().delete()

        self.assertEqual(Tag.objects.all().count(), 1)


@freeze_time("2022-03-22")
class PostTest(TestCase):

    def setUp(self):
        Category.objects.create(
            name='category1', icon='icon1', description='description 1')
        Category.objects.create(
            name='category2', icon='icon2', description='description 2', )
        Category.objects.create(
            name='category 3', icon='icon3', description='description 3',
            parent=Category.objects.first(), is_enabled=False)

        Tag.objects.create(name='Tag 1', icon='Icon 1',
                           description='description 1')
        Tag.objects.create(name='Tag 2', icon='Icon 2',
                           description='description 2')

        Post.objects.create(
            title='Post 1', category=Category.objects.first(), content='Post 1 content')
        Post.objects.create(
            title='Post 2', category=Category.objects.last(), content='Post 2 content')

        Post.objects.first().tag.add(Tag.objects.first())
        Post.objects.last().tag.add(Tag.objects.first())
        Post.objects.last().tag.add(Tag.objects.last())
        # TODO testy dla powiązanycg ćwiczeń

    def test_post_created_successfully(self):
        self.assertEqual(Post.objects.first().title, 'Post 1')
        self.assertEqual(Post.objects.last().title, 'Post 2')
        self.assertEqual(Post.objects.first().category.name,
                         Category.objects.first().name)
        self.assertEqual(Post.objects.last().category.name,
                         Category.objects.last().name)
        self.assertEqual(Post.objects.first().content, 'Post 1 content')
        self.assertEqual(Post.objects.last().content, 'Post 2 content')
        self.assertEqual(Post.objects.first().tag.count(), 1)
        self.assertEqual(Post.objects.last().tag.count(), 2)
        self.assertEqual(
            Post.objects.first().created_at, datetime.datetime(2022, 3, 22, 0, 0, tzinfo=datetime.timezone.utc))
        self.assertEqual(
            Post.objects.last().modified_at, datetime.datetime(2022, 3, 22, 0, 0, tzinfo=datetime.timezone.utc))

    def test_create_post_without_title_raises_error(self):
        with self.assertRaises(Exception):
            Post.objects.create(
                title=None, content='Post content', category=Category.objects.first())

    def test_create_post_without_category_raises_error(self):
        with self.assertRaises(Exception):
            Post.objects.create(
                title='None', content='Post content', category=None)

    def test_update_post_successfull(self):
        post = Post.objects.first()
        post.title = 'New title'
        post.category = Category.objects.last()
        post.content = 'New content'
        post.tag.add(Tag.objects.last())
        post.save()
        self.assertEqual(Post.objects.first().title, 'New title')
        self.assertEqual(Post.objects.first().category,
                         Category.objects.last())
        self.assertEqual(Post.objects.first().content, 'New content')
        self.assertEqual(Post.objects.first().tag.count(), 2)
        self.assertEqual(
            Post.objects.first().created_at, datetime.datetime(2022, 3, 22, 0, 0, tzinfo=datetime.timezone.utc))
        self.assertEqual(
            Post.objects.last().modified_at, datetime.datetime(2022, 3, 22, 0, 0, tzinfo=datetime.timezone.utc))

    def test_delete_post_successfull(self):
        Post.objects.last().delete()
        self.assertEqual(Post.objects.all().count(), 1)
