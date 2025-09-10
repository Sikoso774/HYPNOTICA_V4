# scripts/demarrage_components/resources.py

import pygame
from scripts.demarrage_components.constants import CHEMIN_MUSIQUE_DEMARRAGE, CHEMIN_POLICE_DEMARRAGE

# Cache pour les polices chargées
_font_cache = {}

def load_demarrage_music():
    """
    Charge et retourne le chemin de la musique de démarrage.
    """
    return CHEMIN_MUSIQUE_DEMARRAGE

def get_demarrage_font(size):
    """
    Charge ou récupère une police depuis un cache.
    Utilise la police par défaut des constantes.
    """
    key = (CHEMIN_POLICE_DEMARRAGE, size)
    if key not in _font_cache:
        try:
            _font_cache[key] = pygame.font.Font(CHEMIN_POLICE_DEMARRAGE, size)
        except pygame.error as e:
            print(f"Erreur de chargement de police ({CHEMIN_POLICE_DEMARRAGE}, {size}): {e}")
            _font_cache[key] = pygame.font.Font(None, size) # Police par défaut Pygame
    return _font_cache[key]