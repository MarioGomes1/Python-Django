from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):  # book data entity with a title and rating
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])
    author = models.CharField(null=True, max_length=100)
    is_best_selling = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}, ({self.rating})"
