"""Profile model."""

# Django
from django.db import models

# Models
from api.community.models import Feed, Comment
from api.users.models import Profile

# Utilities
from api.utils.models import DefaultModel
from django_enum_choices.fields import EnumChoiceField
from api.utils.testing import CustomEnum

class ReactionTypes(CustomEnum):
    Like = 1
    Celebrate = 2
    Love = 3
    Insightful = 4
    Curious = 4

class Reaction(DefaultModel):
    """Reaction model.

    A reaction is the way users show what an other user's actions make them feel
    """
    feed = models.ForeignKey(Feed, blank=True, null=True, on_delete=models.CASCADE, related_name='reactions')

    comment = models.ForeignKey(Comment, blank=True, null=True, on_delete=models.CASCADE, related_name='reactions')

    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reactions')

    type = EnumChoiceField(ReactionTypes, blank=True, null=True)

