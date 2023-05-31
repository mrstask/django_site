from django.db import models

from singlepage.models import SinglePage


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SliderItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='slider_images/')
    page = models.ForeignKey(SinglePage, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
