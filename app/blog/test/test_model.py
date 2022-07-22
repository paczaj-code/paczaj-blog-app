
from django.test import TestCase
from blog.models import Post, Category, Tag
from django.contrib.auth.models import User
# Create your tests here.


class BlogModelsTest(TestCase):
    """
    Blog Models Tests
    """

    def setUp(self):
        Category.objects.create(
            name='category1', icon='icon1', description='description 1')
        Category.objects.create(
            name='category2', icon='icon2', description='description 2')

        tag1 = Tag.objects.create(name='tag1', icon='tag_icon1',
                                  description='tag description 1')

        tag2 = Tag.objects.create(name='tag2', icon='tag_icon2',
                                  description='tag description 2')

        post1 = Post.objects.create(title='Post 1 title',
                                    category=Category.objects.first(), content="Post 1 content")
        post1.tag.add(tag1)
        post1.save()
        post2 = Post.objects.create(title='Post 2 title',
                                    category=Category.objects.last(), content="Post 2 content", is_published=False)
        post2.tag.add(tag1)
        post2.tag.add(tag2)
        post2.save()

    def test_create_category_success(self):
        category = Category.objects.first()
        self.assertEqual(category.name, 'category1')
        self.assertEqual(category.icon, 'icon1')
        self.assertEqual(category.description, 'description 1')
        self.assertEqual(category.is_enabled, True)

    def test_update_category(self):
        category = Category.objects.first()
        category.is_enabled = False
        category.name = 'name2'
        category.icon = 'icon2'
        category.description = 'Some description'
        category.save()

        expected_category = Category.objects.first()
        self.assertFalse(expected_category.is_enabled)
        self.assertEqual(expected_category.name, 'name2')
        self.assertEqual(expected_category.icon, 'icon2')
        self.assertEqual(expected_category.description, 'Some description')

    def test_parent_category(self):
        category = Category.objects.first()
        category.parent = Category.objects.last()
        category.save()
        self.assertEqual(category.parent, Category.objects.last())

    def test_create_tag_success(self):
        tag = Tag.objects.first()
        self.assertEqual(tag.name, 'tag1')
        self.assertEqual(tag.icon, 'tag_icon1')
        self.assertEqual(tag.description, 'tag description 1')

    def test_update_tag(self):
        tag = Tag.objects.first()
        tag.name = 'new tag name'
        tag.icon = 'new tag icon'
        tag.description = 'new tag description'
        tag.save()

        expexted_tag = Tag.objects.first()
        self.assertEqual(expexted_tag.name, 'new tag name')
        self.assertEqual(expexted_tag.icon, 'new tag icon')
        self.assertEqual(expexted_tag.description, 'new tag description')

    def test_create_post(self):
        post1 = Post.objects.first()
        self.assertEqual(post1.title, 'Post 1 title')
        self.assertEqual(post1.category.name, 'category1')
        self.assertEqual(post1.content, 'Post 1 content')
        self.assertEqual(post1.tag.count(), 1)
        self.assertTrue(post1.is_published)

        post2 = Post.objects.last()
        self.assertEqual(post2.title, 'Post 2 title')
        self.assertEqual(post2.category.name, 'category2')
        self.assertEqual(post2.content, 'Post 2 content')
        self.assertEqual(post2.tag.count(), 2)
        self.assertFalse(post2.is_published)

    def test_update_post(self):
        post = Post.objects.first()
        post.title = 'New title'
        post.category = Category.objects.last()
        post.content = 'New content'
        post.is_published = False
        post.tag.add(Tag.objects.first())
        post.tag.add(Tag.objects.last())
        post.save()

        expected_post = Post.objects.first()
        self.assertEqual(expected_post.title, 'New title')
        self.assertEqual(expected_post.category.name, 'category2')
        self.assertEqual(expected_post.content, 'New content')
        self.assertFalse(expected_post.is_published)
        self.assertEqual(expected_post.tag.count(), 2)


# TODO testy dla powiązanycg ćwiczeń
