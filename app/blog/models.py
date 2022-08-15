from django.db import models
from django.contrib import admin
from category.models import Category
from django.template.defaultfilters import slugify
import json
import requests


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
    image_id = models.CharField(max_length=255, blank=True, null=True)
    image = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'post'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.image_id:
            result = requests.get(
                f'https://api.unsplash.com/photos/{self.image_id}?client_id=eWnEhgP8URLT8IwJXSsslgayoKT2vkltpdJtfu-vrV8')
            image_data = result.json()
            image_dict = {
                "id": image_data["id"], "urls": image_data["urls"], "user": image_data["user"]}
            self.image = json.dumps(image_dict)
        super().save(*args, **kwargs)


admin.site.register(Post)
admin.site.register(Tag)
