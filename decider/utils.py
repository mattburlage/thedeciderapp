from django.http import Http404

from decider.models import Item


def get_item(item_id):
    try:
        return Item.objects.get(archived=False, pk=item_id)
    except Item.DoesNotExist:
        raise Http404
