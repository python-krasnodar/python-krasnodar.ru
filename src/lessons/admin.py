from django.contrib import admin

from .models import Lesson, Series


class LessonAdmin(admin.ModelAdmin):
    pass


class SeriesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Series, SeriesAdmin)