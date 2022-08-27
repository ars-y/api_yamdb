from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Title, Category
from api_yamdb.settings import ALREDY_LOADED_ERROR_MESSAGE


class Command(BaseCommand):
    help = "Loads data from titles.csv"

    def handle(self, *args, **options):
        if Title.objects.exists():
            print('titles data already exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        for row in DictReader(
            open('static/data/titles.csv', 'r', encoding='utf-8')
        ):
            review = Title(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category=Category.objects.get(pk=int(row['category']))
            )
            review.save()
