from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy, reverse
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/blog_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/blog_detail.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.counter_view += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    model = Post
    template_name = "blog/blog_form.html"
    fields = (
        "title",
        "content",
        "preview",
        "is_published",
    )
    success_url = reverse_lazy("blog:blog_list")


class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/blog_form.html"
    fields = (
        "title",
        "content",
        "preview",
    )
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/blog_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")
