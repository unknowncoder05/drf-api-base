"""Profile serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from api.users.models import Profile

# Serializers
from api.community.serializers import LinkModelSerializer


class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile model serializer."""
    social_links = LinkModelSerializer(read_only=True, many=True)

    class Meta:
        """Meta class."""

        model = Profile
        fields = (
            'picture', 'biography', 'is_public',
            'social_links',
        )
