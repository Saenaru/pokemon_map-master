from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField("Название", max_length=200)
    image = models.ImageField("Изображение", upload_to='pokemon_images/', blank=True, null=True)
    description = models.TextField("Описание", blank=True, null=True)
    title_en = models.CharField("Название на английском", max_length=200, blank=True, null=True)
    title_jp = models.CharField("Название на японском", max_length=200, blank=True, null=True)
    previous_evolution = models.ForeignKey(
        'self', 
        verbose_name='Из кого эволюционирует',
        related_name='next_evolution',
        on_delete=models.SET_NULL,
        null=True, 
        blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.CASCADE, related_name='entities')
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")
    appeared_at = models.DateTimeField("Время появления", blank=True, null=True)
    disappeared_at = models.DateTimeField("Время исчезновения", blank=True, null=True)
    level = models.IntegerField("Уровень", blank=True, null=True)
    health = models.IntegerField("Здоровье", blank=True, null=True)
    attack = models.IntegerField("Атака", blank=True, null=True)
    defense = models.IntegerField("Защита", blank=True, null=True)
    stamina = models.IntegerField("Выносливость", blank=True, null=True)

    def __str__(self):
        return f"{self.pokemon.title} at ({self.lat}, {self.lon})"
