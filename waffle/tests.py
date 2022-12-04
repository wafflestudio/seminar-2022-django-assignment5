from django.test import TestCase

from django.db.models import QuerySet

from rest_framework import serializers
from waffle.models import Comment, Post
from waffle.serializers import UserSerializer, CommentSerializer, PostSerializer
from waffle.services import LoadDataService


class TheLastTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        load_data_service = LoadDataService()
        load_data_service.load_data()

    def get_a_queryset(self) -> QuerySet:
        return CommentSerializer.prefetch_user(Comment.objects.all())

    def get_b_queryset(self) -> QuerySet:
        return CommentSerializer.prefetch_queryset(Comment.objects.all())

    def get_c_queryset(self) -> QuerySet:
        return PostSerializer.prefetch_queryset(Post.objects.all())

    def test_a(self):
        class CommentSerializer(serializers.ModelSerializer):
            created_by = UserSerializer(read_only=True)

            class Meta:
                model = Comment
                fields = ('id', 'created_by', 'post', 'content')

        comment_qs = self.get_a_queryset()[:10]

        with self.assertNumQueries(1):
            serializer = CommentSerializer(comment_qs, many=True)
            serializer.data

    def test_b(self):
        comment_qs = self.get_b_queryset()[:10]

        with self.assertNumQueries(2):
            serializer = CommentSerializer(comment_qs, many=True)
            serializer.data

    def test_c(self):
        post_qs = self.get_c_queryset()[:10]

        with self.assertNumQueries(4):
            serializer = PostSerializer(post_qs, many=True)
            serializer.data
