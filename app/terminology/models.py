from django.db import models
from django.contrib import admin
from category.models import Category
from django.template.defaultfilters import slugify


class Term(models.Model):
    definition = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(
        Category, related_name='term_category', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.definition

    def save(self, *args, **kwargs):
        self.slug = slugify(self.definition)
        super().save(*args, **kwargs)


admin.site.register(Term)
