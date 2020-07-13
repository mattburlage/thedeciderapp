from django.contrib.auth.models import User
from django.db import models


class Campaign(models.Model):
    name = models.CharField(max_length=64)
    code = models.SlugField(max_length=64)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='owned_campaigns')
    subscribers = models.ManyToManyField(User, blank=True, related_name='campaigns')

    yes_vote = models.CharField(max_length=16, default="Yes")
    no_vote = models.CharField(max_length=16, default="No")

    @property
    def all_users(self):
        return self.subscribers.all() | User.objects.filter(pk=self.owner_id)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(null=True, blank=True, max_length=64)
    text = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to="vote-images/", null=True, blank=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    archived = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.campaign})"


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='votes')
    vote = models.NullBooleanField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.item} - {self.user} - {'Yes' if self.vote else 'No'}"
