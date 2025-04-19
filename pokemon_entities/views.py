import folium
import json
from .models import Pokemon, PokemonEntity
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    current_time = timezone.now()
    pokemons = Pokemon.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    
    for pokemon in pokemons:
        entities = pokemon.entities.all()
        for entity in entities:
            if (
                (entity.appeared_at is None or entity.appeared_at <= current_time) and
                (entity.disappeared_at is None or entity.disappeared_at >= current_time)
            ):
                img_url = request.build_absolute_uri(pokemon.image.url) if pokemon.image else DEFAULT_IMAGE_URL
                add_pokemon(folium_map, entity.lat, entity.lon, img_url)

    pokemons_on_page = []
    for pokemon in pokemons:
        img_url = request.build_absolute_uri(pokemon.image.url) if pokemon.image else DEFAULT_IMAGE_URL
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': img_url,
            'title': pokemon.title,
        })
    
    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    
    current_time = timezone.now()
    pokemon_entities = PokemonEntity.objects.filter(
        pokemon=pokemon,
        appeared_at__lte=current_time,
        disappeared_at__gte=current_time
    )

    img_url = request.build_absolute_uri(pokemon.image.url) if pokemon.image else DEFAULT_IMAGE_URL
    pokemon_data = {
        'pokemon_id': pokemon.id,
        'img_url': img_url,
        'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description,
        'previous_evolution': None,
        'next_evolution': None
    }

    if pokemon.previous_evolution:
        prev_pokemon = pokemon.previous_evolution
        pokemon_data['previous_evolution'] = {
            'pokemon_id': prev_pokemon.id,
            'title_ru': prev_pokemon.title,
            'img_url': request.build_absolute_uri(prev_pokemon.image.url) if prev_pokemon.image else DEFAULT_IMAGE_URL,
        }

    next_evolutions = pokemon.next_evolution.all()
    if next_evolutions:
        next_pokemon = next_evolutions.first()
        pokemon_data['next_evolution'] = {
            'pokemon_id': next_pokemon.id,
            'title_ru': next_pokemon.title,
            'img_url': request.build_absolute_uri(next_pokemon.image.url) if next_pokemon.image else DEFAULT_IMAGE_URL,
        }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for entity in pokemon_entities:
        add_pokemon(folium_map, entity.lat, entity.lon, img_url)
    
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(),
        'pokemon': pokemon_data
    })