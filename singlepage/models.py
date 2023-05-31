from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.text import slugify
from django.utils.html import strip_tags


class SinglePage(models.Model):
    title = models.CharField(max_length=200)
    seo_title = models.CharField(max_length=200, blank=True, null=True)
    seo_description = models.CharField(max_length=300, blank=True, null=True)
    seo_keywords = models.CharField(max_length=300, blank=True, null=True)
    body = RichTextUploadingField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.seo_title:
            self.seo_title = self.title[:60]

        if not self.seo_description:
            stripped_body = strip_tags(self.body)
            self.seo_description = stripped_body[:160]

        if not self.seo_keywords:
            self.seo_keywords = ', '.join(slugify(self.title).split('-'))

        super().save(*args, **kwargs)
