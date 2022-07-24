
from distutils import text_file
from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify
# from practice.models import Practice


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    icon = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_enabled = models.BooleanField(default=True)
    parent = models.ForeignKey(
        'Category', related_name='parent_category', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
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


class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        'Category', related_name='category', on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
