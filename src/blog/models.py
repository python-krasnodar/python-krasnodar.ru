from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Tag(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    content = RichTextUploadingField()
    cover = models.ImageField(upload_to='post', default=None, null=True, blank=False)
    preview = RichTextField(default=None, null=True, blank=False)
    slug = models.SlugField(max_length=128)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
