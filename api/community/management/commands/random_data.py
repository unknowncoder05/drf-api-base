from django.core.management.base import BaseCommand

# Factories
from api.users.factories.generators import user_generator
from api.community.factories.generators import feed_generator

# Utilites
import factory.random
from random import seed, randrange, random


class Command(BaseCommand):
    help = 'Generates random data for api manual testing'

    def handle(self, *args, **options):
        populate_database()


def populate_database():
    seed(1)
    factory.random.reseed_random('random_data')
    print('creating users')
    users = user_generator(10)

    """
    print('creating feed')
    feed_generator(feeds, users)
    """