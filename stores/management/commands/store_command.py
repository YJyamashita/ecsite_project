from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **option):
        print('storeのバッチを実行')
