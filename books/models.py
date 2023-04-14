from django.db import models
from django.conf import settings
from django.utils.text import slugify


# Create your models here.

class Book(models.Model):
    class LanguageTypes(models.TextChoices):
        UZBEK = 'uzbek', 'Uzbek'
        RUSSIAN = 'russian', 'Russian'
        ENGLISH = 'english', 'English'

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.FloatField()
    sale_parent = models.PositiveSmallIntegerField(default=0)
    best_seller = models.BooleanField(default=False)
    pub_year = models.PositiveIntegerField(null=True)
    page_size = models.PositiveIntegerField()
    lang = models.CharField(max_length=50, choices=LanguageTypes.choices)
    file = models.FileField()
    image = models.ImageField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='books')
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="books")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
