from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Genre
from api_yamdb.settings import ALREDY_LOADED_ERROR_MESSAGE


class Command(BaseCommand):
    help = "Loads data from genre.csv"

    def handle(self, *args, **options):
        if Genre.objects.exists():
            print('genre data already exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        for row in DictReader(open('static/data/genre.csv', 'r', encoding='utf-8')):
            review=Genre(
                id=row['id'],
                name=row['name'],
                slug=row['slug']
            )  
            review.save()
