from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from waffle.services import LoadDataService

USER_NUM = 5
POST_NUM = 2000
COMMENT_NUM = 2000
TAG_NUM = 500

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        load_data_service = LoadDataService(lambda log: self.stdout.write(self.style.SUCCESS(log)))

        if load_data_service.get_is_loaded():
            self.stdout.write(self.style.WARNING('이미 데이터 로드가 완료되어 실행되지 않았습니다.'))
            return

        load_data_service.load_data()
