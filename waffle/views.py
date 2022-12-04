from rest_framework import generics

from waffle.models import Post
from waffle.serializers import PostSerializer


class Get10View(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return PostSerializer.prefetch_queryset(Post.objects.all())[:10]


class GetAllView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return PostSerializer.prefetch_queryset(Post.objects.all())
