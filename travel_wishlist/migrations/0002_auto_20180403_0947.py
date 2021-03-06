# Generated by Django 2.0.3 on 2018-04-03 14:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('travel_wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='comment',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='date_visited',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
