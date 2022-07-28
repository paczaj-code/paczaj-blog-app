
from distutils import text_file
from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify


class Category(models.Model):
    """Model for post categories"""

    POST = 'P'
    PRACTISE = 'E'
    TERM = 'T'
    CHOICES = (
        (POST, "Post"),
        (PRACTISE, "Practise"),
        (TERM, "Terminology"),
    )
    name = models.CharField(max_length=150, unique=True)
    category_type = models.CharField(
        max_length=1, choices=CHOICES, default=POST)
    icon = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_enabled = models.BooleanField(default=True)
    parent = models.ForeignKey(
        'Category', related_name='subcategories', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


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


class Post(models.Model):
    """Model for posts"""
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(
        'Category', related_name='category', on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    tag = models.ManyToManyField(Tag)
    demo_css = models.TextField(null=True, blank=True)
    demo_js = models.TextField(null=True, blank=True)
# TODO add related posts to Post model

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
