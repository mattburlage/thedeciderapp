# Generated by Django 3.0.8 on 2020-07-13 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('decider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='campaign',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='decider.Campaign'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campaign',
            name='subscribers',
            field=models.ManyToManyField(blank=True, related_name='campaigns', to=settings.AUTH_USER_MODEL),
        ),
    ]
