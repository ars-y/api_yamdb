from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import User
from api_yamdb.settings import ALREDY_LOADED_ERROR_MESSAGE


class Command(BaseCommand):
    help = "Loads data from users.csv"

    def handle(self, *args, **options):
        if User.objects.exists():
            print('user data already exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        for row in DictReader(open('static/data/users.csv', 'r', encoding='utf-8')):
            review=User(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                bio=row['bio'],
                first_name=row['first_name'],
                last_name=row['last_name']
            )  
            review.save()
