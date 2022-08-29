from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import GenreTitle, Title, Genre
from api_yamdb.settings import ALREDY_LOADED_ERROR_MESSAGE


class Command(BaseCommand):
    help = "Loads data from genre_title.csv"

    def handle(self, *args, **options):
        if GenreTitle.objects.exists():
            self.stdout.write('genre_title data already exiting.')
            self.stdout.write(ALREDY_LOADED_ERROR_MESSAGE)
            return

        for row in DictReader(
            open('static/data/genre_title.csv', 'r', encoding='utf-8')
        ):
            review = GenreTitle(
                id=row['id'],
                title=Title.objects.get(pk=int(row['title_id'])),
                genre=Genre.objects.get(pk=int(row['genre_id']))
            )
            review.save()
