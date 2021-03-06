# Generated by Django 3.0.8 on 2020-07-13 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('decider', '0003_campaign_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owned_campaigns', to=settings.AUTH_USER_MODEL),
        ),
    ]
