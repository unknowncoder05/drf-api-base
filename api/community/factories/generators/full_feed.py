from api.community.factories import CommentFactory, FeedReactionFactory, CommentReactionFactory
from api.utils.models import save_save
from random import random, choice, randrange, sample

COMMNETS_GENERATION_MAX_DEPTH = 3
RESPONSE_PROBABILITY = 10/100
GENERATION_MAX_RESPONSES = 5
REACTION_PROBABILITY = 30/100
GENERATION_MAX_REACTIONS = 10


def feed_generator(feeds:list, users:list): 
    """
    feeds: list(Feed)
    users: list(User)
    """
    for feed in feeds:
        random_feed_reactions(users, feed=feed)
        random_inception_responses_and_reactions(users, feed)


def feed_inception(created_by_user, feed, users:list, parent=None, depth=1):
    comment = CommentFactory(created_by=created_by_user.profile, feed=feed, parent=parent)
    if depth < COMMNETS_GENERATION_MAX_DEPTH:
        if random() < RESPONSE_PROBABILITY: # probability of having a response
            max_responses = min(GENERATION_MAX_RESPONSES, len(users))
            for user in sample(users, randrange(1, max_responses)):
                feed_inception(user, feed, users, parent=comment, depth=depth+1)
    random_comment_reactions(users, comment=comment)

def random_comment_reactions(users, comment):
    if random() < REACTION_PROBABILITY: # probability of having reactions
        max_reactions = min(GENERATION_MAX_REACTIONS, len(users))
        for user in sample(users, randrange(1, max_reactions)):
            CommentReactionFactory(created_by=user.profile, comment=comment)
        
def random_feed_reactions(users, feed):
    if random() < REACTION_PROBABILITY: # probability of having reactions
        max_reactions = min(GENERATION_MAX_REACTIONS, len(users))
        for user in sample(users, randrange(1, max_reactions)):
            FeedReactionFactory(created_by=user.profile, feed=feed)

def random_inception_responses_and_reactions(users:list, feed):
    if random() < RESPONSE_PROBABILITY:
        max_responses = min(GENERATION_MAX_RESPONSES, len(users))
        for user in sample(users, randrange(1, max_responses)):
            feed_inception(user, feed, users)