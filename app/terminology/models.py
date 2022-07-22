from django.db import models
from django.contrib import admin


class Term(models.Model):
    definition = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.definition


admin.site.register(Term)
