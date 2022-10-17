from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username='myuser').exists():
            User.objects.create_superuser('myuser',
                                          'myuser@myemail.com',
                                          'mypassword')
            print("Superuser created")
        print("Custom superuser already exists")

