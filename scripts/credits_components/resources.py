# scripts/credits_components/resources.py

import pygame
from scripts.credits_components.constants import (
    CHEMIN_IMAGE_CREDITS, CHEMIN_MUSIQUE_CREDITS,
    LARGEUR_ECRAN_CREDITS, HAUTEUR_ECRAN_CREDITS,
    CREDITS_CONTENT # On a besoin de la liste de contenu pour charger les images qu'elle référence
)

def load_credits_resources():
    """
    Charge l'image de fond principale et la musique des crédits.
    Redimensionne l'image si nécessaire.
    Retourne (image_credits, music_path, loaded_font_cache).
    """
    loaded_images = {}
    music_path = CHEMIN_MUSIQUE_CREDITS

    # Charger l'image principale référencée dans CREDITS_CONTENT
    for item in CREDITS_CONTENT:
        if item['type'] == 'image' and 'image_path' in item:
            try:
                img = pygame.image.load(item['image_path']).convert_alpha()
                # Redimensionnement selon le facteur d'échelle défini dans les constantes
                scaled_width = int(LARGEUR_ECRAN_CREDITS * item.get('image_scale_factor', 1))
                scaled_height = int(HAUTEUR_ECRAN_CREDITS * item.get('image_scale_factor', 1))
                img = pygame.transform.scale(img, (scaled_width, scaled_height))
                loaded_images[item['value']] = img
            except pygame.error as e:
                print(f"Erreur de chargement d'image pour les crédits ({item['image_path']}): {e}")
                loaded_images[item['value']] = pygame.Surface((1, 1), pygame.SRCALPHA) # Image vide

    return loaded_images, music_path

# Cache des polices chargées pour éviter de recharger la même police plusieurs fois
_font_cache = {}

def get_credits_font(font_path, size):
    """
    Charge ou récupère une police depuis un cache.
    """
    key = (font_path, size)
    if key not in _font_cache:
        try:
            _font_cache[key] = pygame.font.Font(font_path, size)
        except pygame.error as e:
            print(f"Erreur de chargement de police ({font_path}, {size}): {e}")
            _font_cache[key] = pygame.font.Font(None, size) # Police par défaut
    return _font_cache[key]