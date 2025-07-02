from django.urls import path
from blog.apps import BlogConfig

from blog.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("", PostListView.as_view(), name="blog_list"),
    path("blog/<int:pk>/", PostDetailView.as_view(), name="blog_detail"),
    path("blog/create/", PostCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/update/", PostUpdateView.as_view(), name="blog_update"),
    path("blog/<int:pk>/delete/", PostDeleteView.as_view(), name="blog_delete"),
]
