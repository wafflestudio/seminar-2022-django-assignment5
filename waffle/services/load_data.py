import random
import typing

from django.contrib.auth import get_user_model
from model_mommy import mommy

from waffle.models import Tag, Post, Comment

USER_NUM = 5
POST_NUM = 2000
COMMENT_NUM = 2000
TAG_NUM = 500

User = get_user_model()


class LoadDataService:
    def __init__(self, log: typing.Callable[[str], None] = lambda: None):
        self.log = log

    def get_is_loaded(self):
        return (
                User.objects.count() >= USER_NUM and
                Post.objects.count() >= POST_NUM and
                Comment.objects.count() >= COMMENT_NUM and
                Tag.objects.count() >= TAG_NUM
        )

    def load_data(self):
        tags = mommy.make(Tag, _quantity=TAG_NUM)
        self.log(f'TAG {TAG_NUM}개 생성 완료.')

        mommy.make(User, _quantity=USER_NUM)
        self.log(f'User {USER_NUM}개 생성 완료.')

        users = User.objects.all()

        for _ in range(POST_NUM):
            mommy.make(Post, created_by=random.choice(users), tags=random.choices(tags))
        self.log(f'Post {POST_NUM}개 생성 완료.')

        posts = Post.objects.all()

        for _ in range(COMMENT_NUM):
            mommy.make(Comment, created_by=random.choice(users),
                       post=random.choice(posts),
                       tags=random.choices(tags))
        self.log(f'Comment {COMMENT_NUM}개 생성 완료.')
