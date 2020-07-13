from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

from decider.models import Campaign

models = apps.get_models()


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    filter_horizontal = ['subscribers']


app_models = apps.get_app_config('decider').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
