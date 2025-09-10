# scripts/ecran_titre_components/text_utils.py (ou crée un nouveau fichier comme scripts/text_display_utils.py si tu préfères)

import pygame
from scripts.ecran_titre_components.constants import CHEMIN_POLICE # Assure-toi que CHEMIN_POLICE est correct

_font_cache = {} # Cache pour les polices

def get_cached_font(font_path, font_size):
    key = (font_path, font_size)
    if key not in _font_cache:
        try:
            _font_cache[key] = pygame.font.Font(font_path, font_size)
        except pygame.error:
            # Fallback à une police Pygame par défaut si le chemin est invalide
            _font_cache[key] = pygame.font.Font(None, font_size)
    return _font_cache[key]


def afficher_texte_centre(surface, texte, couleur, y_position, font_path=None, font_size=30, max_chars_to_display=-1):
    """
    Affiche du texte centré horizontalement sur une surface Pygame.
    Permet d'afficher un nombre limité de caractères pour l'effet de frappe.

    Args:
        surface (pygame.Surface): La surface sur laquelle dessiner.
        texte (str): Le texte à afficher.
        couleur (tuple): La couleur du texte (R, G, B).
        y_position (int): La coordonnée Y du centre vertical du texte.
        font_path (str, optional): Chemin vers le fichier de police TTF. Par défaut, utilise la police du module.
        font_size (int, optional): Taille de la police. Par défaut à 30.
        max_chars_to_display (int, optional): Nombre maximal de caractères à afficher.
                                              Si -1, affiche tout le texte.
    """
    font_path_to_use = font_path if font_path else CHEMIN_POLICE
    police = get_cached_font(font_path_to_use, font_size)

    # Applique le max_chars_to_display
    texte_a_afficher = texte[:max_chars_to_display]

    texte_surface = police.render(texte_a_afficher, True, couleur)
    texte_rect = texte_surface.get_rect(center=(surface.get_width() // 2, y_position))
    surface.blit(texte_surface, texte_rect)