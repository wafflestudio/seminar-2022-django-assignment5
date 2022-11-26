import random

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from model_mommy import mommy

from waffle.models import Comment, Post, Tag

USER_NUM = 5
POST_NUM = 2000
COMMENT_NUM = 2000
TAG_NUM = 500

User = get_user_model()


class Command(BaseCommand):
    def get_is_loaded(self):
        return (
                User.objects.count() >= USER_NUM and
                Post.objects.count() >= POST_NUM and
                Comment.objects.count() >= COMMENT_NUM and
                Tag.objects.count() >= TAG_NUM
        )

    def handle(self, *args, **options):
        if self.get_is_loaded():
            self.stdout.write(self.style.WARNING('이미 데이터 로드가 완료되어 실행되지 않았습니다.'))
            return

        tags = mommy.make(Tag, _quantity=TAG_NUM)
        self.stdout.write(self.style.SUCCESS(f'TAG {TAG_NUM}개 생성 완료.'))

        mommy.make(User, _quantity=USER_NUM)
        self.stdout.write(self.style.SUCCESS(f'User {USER_NUM}개 생성 완료.'))

        users = User.objects.all()

        for _ in range(POST_NUM):
            mommy.make(Post, created_by=random.choice(users), tags=random.choices(tags))
        self.stdout.write(self.style.SUCCESS(f'Post {POST_NUM}개 생성 완료.'))

        posts = Post.objects.all()

        for _ in range(COMMENT_NUM):
            mommy.make(Comment, created_by=random.choice(users),
                       post=random.choice(posts),
                       tags=random.choices(tags))
        self.stdout.write(self.style.SUCCESS(f'Comment {COMMENT_NUM}개 생성 완료.'))
