# Generated by Django 3.0.8 on 2020-07-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decider', '0006_auto_20200713_0332'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]