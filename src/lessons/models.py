from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Series(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
    description = RichTextField(blank=True, null=True, default=None)
    cover = models.ImageField(upload_to='series')
    slug = models.SlugField(max_length=128, blank=False, null=False, default='')
    position = models.IntegerField(blank=False, null=False, default=0)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    preview = RichTextField(blank=False, null=False, default=None)
    content = RichTextUploadingField(blank=False, null=False)
    series = models.ForeignKey(Series)
    position = models.IntegerField(default=0)
    slug = models.SlugField(blank=False, null=False, default='')

    def __str__(self):
        return self.title
