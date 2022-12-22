from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    tags = models.ManyToManyField(through='PostToTag', to='Tag')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    content = models.TextField()
    tags = models.ManyToManyField(through='CommentToTag', to='Tag')


class PostToTag(models.Model):
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


class CommentToTag(models.Model):
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)


class Tag(models.Model):
    content = models.CharField(max_length=200, primary_key=True)
