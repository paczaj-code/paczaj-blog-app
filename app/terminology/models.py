from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify


class Term(models.Model):
    definition = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.definition

    def save(self, *args, **kwargs):
        self.slug = slugify(self.definition)
        super().save(*args, **kwargs)


admin.site.register(Term)
