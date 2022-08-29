from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Comment, Review, User
from api_yamdb.settings import ALREDY_LOADED_ERROR_MESSAGE


class Command(BaseCommand):
    help = "Loads data from comments.csv"

    def handle(self, *args, **options):
        if Comment.objects.exists():
            self.stdout.write('comments data already exiting.')
            self.stdout.write(ALREDY_LOADED_ERROR_MESSAGE)
            return

        for row in DictReader(
            open('static/data/comments.csv', 'r', encoding='utf-8')
        ):
            review = Comment(
                id=row['id'],
                review=Review.objects.get(pk=int(row['review_id'])),
                text=row['text'],
                author=User.objects.get(pk=int(row['author'],)),
                pub_date=row['pub_date']
            )
            review.save()
