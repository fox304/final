from django.contrib.auth.models import User
from django.core.management import BaseCommand

from myrecipes.forms import RecipeForm
from myrecipes.models import Recipe


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(Recipe.objects.all())
