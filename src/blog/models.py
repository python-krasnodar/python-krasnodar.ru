from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    content = RichTextUploadingField()
    slug = models.SlugField(max_length=128)

    def __str__(self):
        return self.title
