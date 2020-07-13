from django.http import Http404

from decider.models import Item


def get_item(item_id, archived=False):
    # try:
        if archived:
            return Item.objects.get(pk=item_id)
        else:
            return Item.objects.get(archived=False, pk=item_id)
    # except Item.DoesNotExist:
    #     raise Http404('get_item item dne')
