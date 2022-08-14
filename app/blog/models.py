
from distutils import text_file
from django.db import models
from django.contrib import admin
from category.models import Category
from django.template.defaultfilters import slugify


class Tag(models.Model):
    """Model for post tags"""
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        db_table = 'tag'


class Post(models.Model):
    """Model for posts"""
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(
        Category, related_name='post_category', on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    tag = models.ManyToManyField(Tag)
    demo_css = models.TextField(null=True, blank=True)
    demo_js = models.TextField(null=True, blank=True)
    related_posts = models.ManyToManyField('Post', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'post'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


admin.site.register(Post)
admin.site.register(Tag)
