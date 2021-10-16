"""Feed serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from api.community.models import Feed


class FeedModelSerializer(serializers.ModelSerializer):
    """Read Feed model serializer."""

    class Meta:
        """Meta class."""

        model = Feed
        fields = (
            'id', 'reactions', 'comments'
        )
