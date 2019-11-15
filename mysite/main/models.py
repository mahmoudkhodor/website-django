from django.db import models
from datetime import datetime

# Create your models here.


class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)


class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField(
        "date published", default=datetime.now())

    def __str__(self):
        return self.tutorial_title
