from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Review, User, Title
from api_yamdb.settings import ALREDY_LOADED_ERROR_MESSAGE


class Command(BaseCommand):
    help = "Loads data from review.csv"

    def handle(self, *args, **options):
        if Review.objects.exists():
            self.stdout.write('review data already exiting.')
            self.stdout.write(ALREDY_LOADED_ERROR_MESSAGE)
            return

        for row in DictReader(
            open('static/data/review.csv', 'r', encoding='utf-8')
        ):
            review = Review(
                id=row['id'],
                title=Title.objects.get(pk=int(row['title_id'])),
                text=row['text'],
                author=User.objects.get(id=int(row['author'])),
                score=row['score'],
                pub_date=row['pub_date'],
            )
            review.save()
