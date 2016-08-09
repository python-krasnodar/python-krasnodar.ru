from django.views.generic import ListView, DetailView

from .models import Post, Tag


class PostList(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()[:15]
        return context


class PostDetail(DetailView):
    model = Post
