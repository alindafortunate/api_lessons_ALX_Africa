from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title}"
