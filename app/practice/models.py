from django.db import models
from blog.models import Category, Post
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Practice(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    exercise = models.TextField()
    solution = models.TextField()
    related_posts = models.ManyToManyField(Post)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'practice_exercise'


class UserSolution(models.Model):
    solution = models.TextField()
    user = models.ForeignKey(User, related_name='user',
                             on_delete=models.SET_NULL,  blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    practise = models.ForeignKey(
        'Practice', related_name='practise', on_delete=models.SET_NULL, blank=True, null=True)

    is_public = models.BooleanField(default=False)

    class Meta:
        db_table = 'practice_user_solution'
