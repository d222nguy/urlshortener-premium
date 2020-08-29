from django.core.management.base import BaseCommand, CommandError
from shortener.models import URL
class Command(BaseCommand):
    help = 'Refresh all URL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        print(options)
        return URL.objects.refresh_shortcode(items = options['items'])
