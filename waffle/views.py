from django.shortcuts import render
from django.db.models import Prefetch
from rest_framework import generics

from waffle.models import Post, Comment
from waffle.serializers import PostSerializer


class Get10View(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.select_related(
            'created_by'
        ).prefetch_related(
            'tags',
            Prefetch(
                'comment_set',
                queryset=Comment.objects.select_related(
                    'created_by').prefetch_related('tags'),
                to_attr='prefetched_comment_set'
            )
        )[:10]


class GetAllView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()
