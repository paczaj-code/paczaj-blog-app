from django.db import models
from blog.models import Post
from django.contrib.auth.models import User
# Create your models here.

# class Meta:
#     db_table = ''
#     managed = True
#     verbose_name = 'ModelName'
#     verbose_name_plural = 'ModelNames'


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        db_table = 'practice_category'
        # managed = True


class Practice(models.Model):
    name = models.CharField(max_length=255)
    exersise = models.TextField()
    solution = models.TextField()
    related_posts = models.ManyToManyField(Post)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(
        User, related_name='author', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'practice_exercise'


class UserSolution(models.Model):
    solution = models.TextField()
    user = models.ForeignKey(User, related_name='user',
                             on_delete=models.SET_NULL,  blank=True, null=True)
    practise = models.ForeignKey(
        'Practice', related_name='practise', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'practice_user_solution'
