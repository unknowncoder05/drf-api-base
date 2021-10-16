"""Profile model."""

# Django
from django.db import models

# Models
from api.users.models import Profile
from api.community.models import Feed

# Utilities
from api.utils.models import DefaultModel


class Comment(DefaultModel):
    """Comment model.

    A comment the way an user expresses its ideas from other users actions
    """
    feed = models.ForeignKey(Feed, blank=True, null=True, on_delete=models.CASCADE, related_name='comments')

    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, related_name='child_comments')

    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')

    content = models.CharField(max_length=300)