# scripts/sfx_manager.py

import pygame
from scripts.paths import get_resource_path

# Cache pour les effets sonores chargés
_sfx_cache = {}

def load_sfx(sound_path):
    """
    Charge un effet sonore et le met en cache pour éviter les rechargements.
    """
    if sound_path not in _sfx_cache:
        try:
            full_path = get_resource_path(sound_path)
            _sfx_cache[sound_path] = pygame.mixer.Sound(full_path)
        except pygame.error as e:
            print(f"Erreur de chargement du son '{sound_path}': {e}")
            _sfx_cache[sound_path] = None # Mettre None pour ne pas réessayer de charger
    return _sfx_cache[sound_path]

def play_sfx(sound_path, volume=1.0):
    """
    Joue un effet sonore. Le son doit d'abord être chargé via load_sfx.
    """
    sfx = load_sfx(sound_path)
    if sfx:
        sfx.set_volume(volume)
        sfx.play()