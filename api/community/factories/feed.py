# Models
from api.community.models import Feed

# Utils
from factory.django import DjangoModelFactory



# Factory
class FeedFactory(DjangoModelFactory):
    class Meta:
        model = Feed