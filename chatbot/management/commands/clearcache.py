# your_app
from django.core.management.base import BaseCommand
from django.core.cache import cache

class Command(BaseCommand):
    help = 'Clears all entries from the Django cache.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Attempting to clear cache...'))

        try:
            cache.clear()
            self.stdout.write(self.style.SUCCESS('Cache cleared successfully!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error clearing cache: {e}'))

