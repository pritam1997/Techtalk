from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    num_pages = models.IntegerField(default=0)
    isbn13 = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return self.title
