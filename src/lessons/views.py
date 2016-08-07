from django.views.generic import ListView, DetailView

from .models import Series, Lesson


class SeriesListView(ListView):
    model = Series


class SeriesDetailView(DetailView):
    model = Series


class LessonDetailView(DetailView):
    model = Lesson
