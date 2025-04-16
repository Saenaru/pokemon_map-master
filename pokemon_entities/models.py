from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pokemon_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entities')
    lat = models.FloatField("Latitude")
    lon = models.FloatField("Longitude")
    appeared_at = models.DateTimeField("Appearance Time", blank=True, null=True)
    disappeared_at = models.DateTimeField("Disappearance Time", blank=True, null=True)
    level = models.IntegerField("Level", blank=True, null=True)
    health = models.IntegerField("Health", blank=True, null=True)
    attack = models.IntegerField("Attack", blank=True, null=True)
    defense = models.IntegerField("Defense", blank=True, null=True)
    stamina = models.IntegerField("Stamina", blank=True, null=True)

    def __str__(self):
        return f"{self.pokemon.title} at ({self.lat}, {self.lon})"