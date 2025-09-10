# scripts/instructions_components/resources.py

import pygame
from scripts.instructions_components.constants import CHEMIN_POLICE_INSTRUCTIONS

_font_cache = {}

def get_instructions_font(size):
    """
    Charge ou récupère une police depuis un cache.
    """
    key = (CHEMIN_POLICE_INSTRUCTIONS, size)
    if key not in _font_cache:
        try:
            _font_cache[key] = pygame.font.Font(CHEMIN_POLICE_INSTRUCTIONS, size)
        except pygame.error as e:
            print(f"Erreur de chargement de police ({CHEMIN_POLICE_INSTRUCTIONS}, {size}): {e}")
            _font_cache[key] = pygame.font.Font(None, size) # Police par défaut Pygame
    return _font_cache[key]