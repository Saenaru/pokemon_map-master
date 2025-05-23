# Generated by Django 3.1.14 on 2025-04-16 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_auto_20250416_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='attack',
            field=models.IntegerField(blank=True, null=True, verbose_name='Attack'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='defense',
            field=models.IntegerField(blank=True, null=True, verbose_name='Defense'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(blank=True, null=True, verbose_name='Health'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(blank=True, null=True, verbose_name='Level'),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(blank=True, null=True, verbose_name='Stamina'),
        ),
    ]
