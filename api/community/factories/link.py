# Models
from api.community.models import Link

# Utils
import factory
from factory.django import DjangoModelFactory
from api.community.models.reaction import ReactionTypes


# Factories
from api.users.factories import ProfileFactory


# Factory
class LinkFactory(DjangoModelFactory):
    class Meta:
        model = Link
        django_get_or_create = ('url', 'profile')


    description = factory.Fake('sentence', nb_words=3)

    url = factory.Fake('uri')

    profile = factory.SubFactory(ProfileFactory)