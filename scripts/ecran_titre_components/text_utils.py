# scripts/ecran_titre_components/text_utils.py

import pygame
# Importe les constantes par défaut pour la police si aucune n'est spécifiée
from scripts.ecran_titre_components.constants import LARGEUR_ECRAN, CHEMIN_POLICE, TAILLE_POLICE
from scripts.paths import get_resource_path # Nécessaire pour charger la police

# Cache pour stocker les objets police déjà créés (chemin_police, taille) -> objet_police
_font_cache = {}

def afficher_texte_centre(surface, texte, couleur, y, font_path=None, font_size=None):
    """
    Affiche du texte centré horizontalement sur l'écran avec une taille de police spécifique.
    Si font_path ou font_size ne sont pas fournis, les valeurs par défaut de constants.py sont utilisées.

    Args:
        surface (pygame.Surface): La surface sur laquelle dessiner (l'écran).
        texte (str): Le texte à afficher.
        couleur (tuple): La couleur du texte (R, G, B).
        y (int): La coordonnée Y du centre vertical du texte.
        font_path (str, optional): Le chemin vers le fichier de police. Par défaut CHEMIN_POLICE.
        font_size (int, optional): La taille de la police à utiliser. Par défaut TAILLE_POLICE.
    """
    # Détermine le chemin et la taille finale de la police, en utilisant les valeurs par défaut si non spécifiées
    final_font_path = font_path if font_path is not None else CHEMIN_POLICE
    final_font_size = font_size if font_size is not None else TAILLE_POLICE

    # Clé unique pour le cache : (chemin du fichier, taille)
    font_key = (final_font_path, final_font_size)

    # Vérifie si la police de cette taille est déjà en cache
    if font_key not in _font_cache:
        try:
            # Charge la police si elle n'est pas en cache, en utilisant get_resource_path
            abs_font_path = get_resource_path(final_font_path)
            _font_cache[font_key] = pygame.font.Font(abs_font_path, final_font_size)
        except Exception as e:
            print(f"Erreur de chargement de la police '{final_font_path}' de taille {final_font_size}: {e}")
            # En cas d'erreur (fichier non trouvé, etc.), utilise une police système de secours
            _font_cache[font_key] = pygame.font.SysFont(None, final_font_size) # Police par défaut du système

    # Récupère l'objet police du cache
    police_font = _font_cache[font_key]

    # Rend le texte et le positionne au centre
    texte_surface = police_font.render(texte, True, couleur)
    texte_rect = texte_surface.get_rect(center=(LARGEUR_ECRAN // 2, y))
    surface.blit(texte_surface, texte_rect)