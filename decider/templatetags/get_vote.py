from django import template

register = template.Library()


def get_vote(item, user):
    return item.votes.get(user=user).vote


def get_vote_count(item, option):
    return item.votes.filter(vote=option).count()


def get_vote_percent(item, option):
    sub_count = item.campaign.subscribers.all().count()

    if sub_count == 0:
        return 0

    return (get_vote_count(item, option) / sub_count) * 100


register.filter('get_vote', get_vote)
register.filter('get_vote_count', get_vote_count)
register.filter('get_vote_percent', get_vote_percent)
