from django.db import models
from django.contrib import admin
from category.models import Category
from blog.models import Post
# from django.contrib.auth.models import User
# from django.template.defaultfilters import slugify


class Practice(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    related_posts = models.ManyToManyField(Post)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'practice'


class Exercise(models.Model):
    EASY = 'E'
    MEDIUM = 'M'
    DIFFICULT = 'D'
    CHOICES = (
        (EASY, "Easy"),
        (MEDIUM, "Medium"),
        (DIFFICULT, "Difficult"),
    )
    # title = models.CharField(max_length=255)
    number = models.IntegerField()
    practise = models.ForeignKey(Practice, on_delete=models.CASCADE)
    difficulty = models.CharField(
        choices=CHOICES, default=MEDIUM, max_length=1)
    exercise = models.TextField()
    solution = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        last_number = Exercise.objects.filter(
            practise=self.practise).aggregate(Max(number))

        if last_number is None:
            number = 1
        else:
            number = last_number + 1
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'exercise'

    def __str__(self):
        return self.title


# admin.site.register(Exercise)
# admin.site.register(Practice)
