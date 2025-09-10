# scripts/game_elements/resources.py

import pygame
import os
#from scripts.paths import get_resource_path
from scripts.game_elements.constants import (
    CHEMIN_POLICE_JEU, LARGEUR_ECRAN_JEU, HAUTEUR_ECRAN_JEU, GIF_FOLDER_PATH, PHONE_SPRITE_PATH, PLAYER_SPRITE_PATH
)

_font_cache = {}
_gif_images_cache = []

def get_game_font(size):
    """
    Charge ou récupère une police depuis un cache pour le jeu.
    """
    key = (CHEMIN_POLICE_JEU, size)
    if key not in _font_cache:
        try:
            _font_cache[key] = pygame.font.Font(CHEMIN_POLICE_JEU, size)
        except pygame.error as e:
            print(f"Erreur de chargement de police ({CHEMIN_POLICE_JEU}, {size}): {e}")
            _font_cache[key] = pygame.font.Font(None, size) # Fallback à une police par défaut
    return _font_cache[key]

def load_gif_frames():
    """
    Charge et met en cache les images GIF pour l'arrière-plan.
    """
    if not _gif_images_cache: # Charge seulement si le cache est vide
        print(f"Chargement des images GIF depuis : {GIF_FOLDER_PATH}")
        try:
            for filename in sorted(os.listdir(GIF_FOLDER_PATH)):
                if filename.endswith((".png", ".jpg", ".jpeg")):
                    image_path = os.path.join(GIF_FOLDER_PATH, filename)
                    image = pygame.image.load(image_path).convert_alpha() # Garde l'alpha pour la transparence
                    image = pygame.transform.scale(image, (LARGEUR_ECRAN_JEU, HAUTEUR_ECRAN_JEU))
                    _gif_images_cache.append(image)
            if not _gif_images_cache:
                print(f"Aucune image GIF trouvée dans {GIF_FOLDER_PATH}. L'arrière-plan sera vide.")
        except Exception as e:
            print(f"Erreur lors du chargement des images GIF depuis {GIF_FOLDER_PATH}: {e}")
            # Ajouter un placeholder si le chargement échoue
            _gif_images_cache.append(pygame.Surface((LARGEUR_ECRAN_JEU, HAUTEUR_ECRAN_JEU), pygame.SRCALPHA))
            _gif_images_cache[0].fill((0, 0, 50)) # Un fond bleu très foncé par défaut
    return _gif_images_cache

# --- Fonctions pour charger les sprites du joueur et du téléphone ---
def load_player_sprite(player_size):
    """
    Charge et redimensionne le sprite du joueur.
    Utilise un carré placeholder si PLAYER_SPRITE_PATH n'est pas défini.
    """
    if PLAYER_SPRITE_PATH:
        try:
            sprite = pygame.image.load(PLAYER_SPRITE_PATH).convert_alpha()
            return pygame.transform.scale(sprite, (player_size, player_size))
        except pygame.error as e:
            print(f"Erreur de chargement du sprite joueur ({PLAYER_SPRITE_PATH}): {e}. Utilisation du placeholder.")
    # Placeholder: un carré bleu clair
    placeholder = pygame.Surface((player_size, player_size), pygame.SRCALPHA)
    placeholder.fill((50, 50, 200)) # Bleu un peu plus clair
    return placeholder

def load_phone_sprite(phone_size):
    """
    Charge et redimensionne le sprite du téléphone.
    Utilise un cercle placeholder si PHONE_SPRITE_PATH n'est pas défini.
    """
    if PHONE_SPRITE_PATH:
        try:
            sprite = pygame.image.load(PHONE_SPRITE_PATH).convert_alpha()
            return pygame.transform.scale(sprite, (phone_size, phone_size))
        except pygame.error as e:
            print(f"Erreur de chargement du sprite téléphone ({PHONE_SPRITE_PATH}): {e}. Utilisation du placeholder.")
    # Placeholder: un cercle vert
    placeholder = pygame.Surface((phone_size, phone_size), pygame.SRCALPHA)
    pygame.draw.circle(placeholder, (0, 200, 0), (phone_size // 2, phone_size // 2), phone_size // 2)
    return placeholder

# ... Tu pourrais ajouter des fonctions pour charger les sons ici si tu en as
# def load_sound(path):
#     try:
#         return pygame.mixer.Sound(path)
#     except pygame.error as e:
#         print(f"Erreur de chargement du son ({path}): {e}")
#         return None # Retourne None si le son ne peut pas être chargé