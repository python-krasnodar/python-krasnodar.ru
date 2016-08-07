from django.db import models


class Series(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
    description = models.TextField(blank=True, null=True, default=None)
    cover = models.ImageField(upload_to='series')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    preview = models.TextField(blank=False, null=False, default=None)
    content = models.TextField(blank=False, null=False)
    series = models.ForeignKey(Series)
    position = models.IntegerField(default=0)

    def __str__(self):
        return self.title
