from django.core.management.base import BaseCommand
import pandas


class Command(BaseCommand):
    def handle(self, *args, **options):
        return super().handle(*args, **options)