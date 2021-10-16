# Models
from api.community.models import Comment

# Utils
import factory
from factory.django import DjangoModelFactory

# Factories
from api.users.factories import ProfileFactory
from api.community.factories import FeedFactory


# Factory
class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment
        django_get_or_create = ('created_by', 'content', 'parent')


    feed = factory.SubFactory(FeedFactory)

    created_by = factory.SubFactory(ProfileFactory)

    content = factory.Faker('sentence', nb_words=30)