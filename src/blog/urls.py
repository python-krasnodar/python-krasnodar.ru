from django.conf.urls import url

from .views import PostList, PostDetail

urlpatterns = [
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^(?P<slug>[a-z0-9\-]+)/$', PostDetail.as_view(), name='post_detail'),
]
