from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Category
from api_yamdb.settings import ALREDY_LOADED_ERROR_MESSAGE


class Command(BaseCommand):
    help = "Loads data from category.csv"

    def handle(self, *args, **options):
        if Category.objects.exists():
            print('category data already exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        for row in DictReader(
            open('static/data/category.csv', 'r', encoding='utf-8')
        ):
            review = Category(
                id=row['id'],
                name=row['name'],
                slug=row['slug']
            )
            review.save()
