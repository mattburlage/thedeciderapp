from django import template

register = template.Library()


def get_vote(item, user):
    return item.votes.get(user=user).vote


register.filter('get_vote', get_vote)
