# Generated by Django 3.1.14 on 2025-04-19 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_pokemon_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
