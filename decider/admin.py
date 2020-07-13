from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

from decider.models import Campaign


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    filter_horizontal = ['subscribers']

