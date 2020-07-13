from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from decider.forms import AddItemForm, AddItemFormSave
from decider.models import Item, Campaign, Vote
from decider.utils import get_item


@login_required
def index(request):

    context = {
        'campaigns': request.user.campaigns.all() | request.user.owned_campaigns.all()
    }
    return render(request, 'index.html', context)


@login_required
def campaign(request, campaign_code):
    camp = Campaign.objects.get(code=campaign_code)

    if request.GET.get('archived', False):
        items = Item.objects.filter(campaign=camp)
    else:
        items = Item.objects.filter(archived=False, campaign=camp)

    # make sure vote is valid
    if request.user not in camp.all_users:
        raise Http404

    pending = []
    voted = []

    for item in items:
        if item.votes.filter(user=request.user):
            voted.append(item)
        else:
            pending.append(item)

    add_form = None
    if request.user == camp.owner:
        add_form = AddItemForm()

    context = {
        'campaign': camp,
        'pending': pending,
        'voted': voted,
        'add_form': add_form,
    }
    return render(request, 'campaign.html', context)


@login_required
def vote(request, item_id, vote_val):
    item = get_item(item_id)

    # make sure vote is valid
    if item.archived or request.user not in item.campaign.subscribers.all():
        raise Http404

    # discard any old votes
    for cur_vote in Vote.objects.filter(user=request.user, item=item):
        cur_vote.delete()

    Vote.objects.create(
        user=request.user,
        item=item,
        vote=vote_val == 'yes',
    )

    return redirect('campaign', campaign_code=item.campaign.code)


@login_required
def add_item(request, camp_id):
    camp = Campaign.objects.get(pk=camp_id)

    if request.user != camp.owner:
        raise Http404

    data = request.POST.copy()

    data['campaign'] = camp.id

    form = AddItemFormSave(data, request.FILES)

    if form.is_valid():
        form.save()

    return redirect('campaign', campaign_code=camp.code)


@login_required
def clear_vote(request, item_id):
    item = get_item(item_id)

    Vote.objects.filter(user=request.user, item=item).delete()

    return redirect('campaign', campaign_code=item.campaign.code)


def delete_item(request, item_id):
    item = get_item(item_id)
    code = item.campaign.code

    if item.campaign.owner == request.user:
        item.archived = True
        item.save()

    return redirect('campaign', campaign_code=code)
