from django.conf.urls import url

from .views import SeriesListView, SeriesDetailView, LessonDetailView

urlpatterns = [
    url(r'^$', SeriesListView.as_view(), name='series_list'),
    url(r'^(?P<slug>[a-z0-9\-]+)/$', SeriesDetailView.as_view(), name='series_detail'),
    url(r'^(?P<series_slug>[a-z0-9\-]+)/(?P<slug>[a-z0-9\-]+)/$', LessonDetailView.as_view(), name='detail'),
]
