from django.db import models  # noqa F401

class Pokemon(models.Model):
    title = models.CharField("Название", max_length=200)
    image = models.ImageField("Изображение", upload_to='pokemon_images/', blank=True, null=True)
    description = models.TextField("Описание", blank=True, default='')
    title_en = models.CharField("Название на английском", max_length=200, blank=True, default='')
    title_jp = models.CharField("Название на японском", max_length=200, blank=True, default='')
    previous_evolution = models.ForeignKey(
        'self', 
        verbose_name='Из кого эволюционирует',
        related_name='next_evolutions',
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
    level = models.PositiveIntegerField("Уровень", blank=True, null=True)
    health = models.PositiveIntegerField("Здоровье", blank=True, null=True)
    attack = models.PositiveIntegerField("Атака", blank=True, null=True)
    defense = models.PositiveIntegerField("Защита", blank=True, null=True)
    stamina = models.PositiveIntegerField("Выносливость", blank=True, null=True)

    def __str__(self):
        return f"{self.pokemon.title} at ({self.lat}, {self.lon})"
