from django.db import models


class Book(models.Model):

    """
        Model that defines all the properties that a book must have
    """

    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    body = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    genre = models.CharField(max_length=200)
    pages = models.CharField(max_length=200)
    published_at = models.DateField(blank=True, null=True)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return "title: {}, date: {}".format(self.title, self.published_at)


