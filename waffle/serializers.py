from django.contrib.auth import get_user_model
from django.db.models import Prefetch, QuerySet
from rest_framework import serializers

from waffle.models import Post, Tag, Comment

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('content',)


class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Comment
        fields = ('id', 'created_by', 'post', 'content', 'tags')
    
    @classmethod
    def prefetch_user(cls, queryset: QuerySet):
        return queryset.select_related("created_by")

    @classmethod
    def prefetch_tags(cls, queryset: QuerySet):
        return queryset.prefetch_related('tags')

    @classmethod
    def prefetch_queryset(cls, queryset: QuerySet):
        queryset = cls.prefetch_user(queryset)
        queryset = cls.prefetch_tags(queryset)
        return queryset


class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    comment_set = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'created_by', 'tags', 'title', 'description', 'comment_set')
        
    @classmethod
    def prefetch_user(cls, queryset: QuerySet):
        return queryset.select_related("created_by")

    @classmethod
    def prefetch_tags(cls, queryset: QuerySet):
        return queryset.prefetch_related('tags')

    @classmethod
    def prefetch_comments(cls, queryset: QuerySet):
        return queryset.prefetch_related(
            Prefetch(
                "comment_set",
                queryset=CommentSerializer.prefetch_queryset(Comment.objects.all())
            )
        )

    @classmethod
    def prefetch_queryset(cls, queryset: QuerySet):
        queryset = cls.prefetch_user(queryset)
        queryset = cls.prefetch_tags(queryset)
        queryset = cls.prefetch_comments(queryset)
        return queryset
